import nltk
import re

regex = re.compile('[^a-zA-Z]')

def text_clean(full_text: str) -> str:
    word_bag = full_text.split()

    for word in word_bag:
        tmp_word = word.lower()
        
        # Remove non-alpha
        tmp_word = regex.sub('', tmp_word)

        tmp_word 


def text_tokenize(full_text):
