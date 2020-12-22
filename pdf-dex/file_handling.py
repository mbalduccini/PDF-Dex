import os
from pathlib import Path
import PyPDF4
import textract
from utilities.types import PDF

# ---------------------------------------------------------------------------------
# Logging initialization
import logging

logger = logging.getLogger(__name__)
consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.INFO)

# Setup the formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandle.setFormatter(formatter)
logger.addHandler(consoleHandle)

# ---------------------------------------------------------------------------------

def get_pdf_list() -> list:
    '''
    File paths to pdf
    '''
    return [ 
      str(path)
      for path in Path('/data').rglob('*.pdf')]


def read_pdf(file_path: str) -> PDF:
    '''
    Open and reads pdf content
    '''
    full_text = ""
    metadata = None

    try:
        # Attempt to read with PyPDF4
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF4.PdfFileReader(f)
            metadata = pdf_reader.getDocumentInfo()

            for page in pdf_reader.pages:
                full_text += page.extractText()

        # If PyPDF unsuccessful use OCR
        if full_text == "":
            full_text = textract.process(fileurl, method='tesseract', language='eng')
    
    except Exception as e:
        logger.exception(f"There was an exception: {e}")

    return PDF(file_path, full_text, metadata)
