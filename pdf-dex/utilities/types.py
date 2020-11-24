from datetime import datetime
from time import mktime, strptime
from .pdf_datetime import transform_date

class PDF:
    def __init__(self, path, text, metadata):
        self.path = path
        self.metadata = self._format_metadata(metadata)
        self.tokenized_words = None
        self.text = text

    def _format_metadata(self, metadata):
        new_metadata = {}
        
        for key, value in metadata.items():
            tmp_key, tmp_value = {}, {}

            if key[-4:] == "Date":
                tmp_value = transform_date(value)
            else:
                tmp_value = value.strip("/")

            tmp_key = key.strip("/")
            new_metadata[tmp_key] = tmp_value
        
        return new_metadata          

    def __iter__(self):
        yield 'file', self.path
        yield 'metadata', self.metadata
        yield 'tokenized_words', self.tokenized_words