import os
from pathlib import Path
import PyPDF4
import textract
from utilities.types import PDF


def get_pdf_list() -> list:
    '''
    File paths to pdf
    '''
    return [ 
      path.name 
      for path in Path('data').rglob('*.pdf')]


def read_pdf(file_path: str) -> PDF:
    '''
    Open and reads pdf content
    '''
    full_text = ""
    metadata = None

    # Attempt to read with PyPDF4
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF4.PdfFileReader(f)
        metadata = pdf_reader.getDocumentInfo()

        for page in pdf_reader.pages:
            full_text += page.extractText()

    # If PyPDF unsuccessful use OCR
    if full_text == "":
        full_text = textract.process(fileurl, method='tesseract', language='eng')

    return PDF(file_path, full_text, metadata)


if __name__=="__main__":
    curr_PDF = read_pdf(r"PathToPDF.pdf")
    print(curr_PDF.metadata)