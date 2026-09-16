# Image Text Extractor Using Pytesseract

## Project Description

This project is an **Image Text Extractor** developed using Python and Pytesseract. It extracts text from an image using Optical Character Recognition (OCR) and displays the extracted text in a separate output window.

The project demonstrates the integration of the **Pytesseract OCR library** with Python for simple and effective text recognition from images.

## What is OCR?

**OCR (Optical Character Recognition)** is a technology used to identify and convert text present in images into editable and machine-readable text.

For example, if an image contains:

> Computer technology makes our work easier and faster.

OCR can recognize the words in the image and convert them into text.

## Technologies Used

* **Python** – Programming language used to develop the application.
* **Pytesseract** – Python library used to perform OCR.
* **Tesseract OCR** – OCR engine that recognizes text from images.
* **Pillow** – Python Imaging Library used to open and process images.
* **Tkinter** – Used to display the extracted text in a separate window.

## How the Project Works

1. The user provides the path of an image.
2. The program opens the image using Pillow.
3. Pytesseract sends the image to the Tesseract OCR engine.
4. Tesseract recognizes the text present in the image.
5. The extracted text is displayed in a separate output window.
6. The extracted text is also saved in `extracted_text.txt`.

## Project Structure

```text
pytesseract-ocr-project/
│
├── main.py
├── requirements.txt
├── README.md
│
└── images/
    └── samples.png
```

## Installation

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

Tesseract OCR must also be installed on the system.

## How to Run

Run the following command:

```bash
python main.py
```

When prompted for the image path, enter:

```text
images/samples.png
```

## Output

The program displays the extracted text in a separate **OCR Result** window and saves the recognized text to:

```text
extracted_text.txt
```

## Error Handling

The project handles common errors such as:

* Image file not found
* Invalid image file
* Tesseract OCR not found
* Other unexpected errors

## Internship Project Objective

The objective of this project is to demonstrate the **seamless integration of Pytesseract OCR** into a Python application and provide a simple, user-friendly method for extracting text from images.

## Author

**Manjula**
