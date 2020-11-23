from pathlib import Path
import PyPDF4
import textract
import 

def read_elastic_metadata(file_name):
    pass
   

def get_pdf_list() -> list:
    '''
    File paths to pdf
    '''
    return [ path.name for path in Path('data').rglob('*.pdf')]


def read_pdf(file_path: str) -> str:
    '''
    Open and reads pdf content
    '''
    full_text = ""
    
    # Attempt to read with PyPDF4
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF4.PdfFileReader(f)

        for page in pdf_reader.pages:
            full_text += page.extractText()

    # If PyPDF unsuccessful use OCR
    if full_text == "":
        full_text = textract.process(fileurl, method='tesseract', language='eng')

    return full_text


if __name__=="__main__":
    pass