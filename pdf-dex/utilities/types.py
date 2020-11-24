
class PDF:
    def __init__(self, path, text, metadata):
        self.path = path
        self.metadata = metadata
        self.tokenized_words = None
        self.text = text

    def __iter__(self):
        yield 'file', self.path
        yield 'metadata', self.metadata
        yield 'tokenized_words', self.tokenized_words