import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, UnidentifiedImageError
import pytesseract

# Tesseract installation path
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text(image_path):
    try:
        if not os.path.exists(image_path):
            messagebox.showerror("Error", "Image file not found.")
            return

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image).strip()

        # Save extracted text
        with open("extracted_text.txt", "w", encoding="utf-8") as file:
            file.write(text)

        show_output(text)

    except UnidentifiedImageError:
        messagebox.showerror("Error", "Invalid image file.")

    except pytesseract.TesseractNotFoundError:
        messagebox.showerror("Error", "Tesseract OCR was not found.")

    except Exception as error:
        messagebox.showerror("Error", str(error))


def show_output(text):
    output_window = tk.Tk()
    output_window.title("OCR Result")
    output_window.geometry("600x300")

    title_label = tk.Label(
        output_window,
        text="Extracted Text",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=20)

    text_box = tk.Text(
        output_window,
        font=("Arial", 14),
        wrap="word"
    )
    text_box.pack(padx=20, pady=10, fill="both", expand=True)

    if text:
        text_box.insert("1.0", text)
    else:
        text_box.insert("1.0", "No text detected.")

    text_box.config(state="disabled")

    output_window.mainloop()


def main():
    print("===================================")
    print("       IMAGE TEXT EXTRACTOR")
    print("       Using Pytesseract")
    print("===================================")

    image_path = input("Enter the image path: ").strip().strip('"')

    extract_text(image_path)


if __name__ == "__main__":
    main()
