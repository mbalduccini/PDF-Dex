from pathlib import Path
import PyPDF4
import textract


def pdf_list() -> str:
    '''
    Generator that yeilds file paths to pdf
    '''
    for path in Path('data').rglob('*.pdf'):
        yeild path.name


def read_pdf(file_path: str) -> str:
    '''
    Open and reads pdf content
    '''
    full_text = ""
    
    # Attempt to read with PyPDF4
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF4.PdfFileReader(f)

        for page in pdf_reader.pages:
            fulltext += page.extractText()

    # If PyPDF unsuccessful use OCR
    if full_text == "":
        full_text = textract.process(fileurl, method='tesseract', language='eng')

    return full_text
