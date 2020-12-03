from utilities.nltk_import import *
from collections import Counter
import re
import unittest

from elastic_connector import get_elastic_instance, file_exists, insert_file
from file_handling import read_pdf

# ---------------------------------------------------------------------------------
def filter_list(pdf: str) -> str:
    es = get_elastic_instance()
    #filter(lambda files: file_exists(files, es), pdf_list)
    return file_exists(pdf, es)

# ---------------------------------------------------------------------------------
regex = re.compile('[^a-z0-9]')
stop_words = set(stopwords.words('english'))


def text_clean(full_text: str) -> str:
    '''
    Cleans a string 
    '''
    word_bag = full_text.split()
    clean_text = []

    for word in word_bag:
        tmp_word = word.lower()
        tmp_word = regex.sub('', tmp_word)
        
        if tmp_word == '':
            continue

        if not is_stopword(tmp_word):
           clean_text.append(tmp_word)

    lemmantized_list = word_lemmantize(clean_text)

    return lemmantized_list


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def is_stopword(word):
    return word in stop_words


def penn_to_wordnet(tag):
    if is_adjective(tag):
        return wordnet.ADJ
    elif is_noun(tag):
        return wordnet.NOUN
    elif is_adverb(tag):
        return wordnet.ADV
    elif is_verb(tag):
        return wordnet.VERB
    else:
        return None


def word_lemmantize(word_list):
    tags = nltk.pos_tag(word_list)
    lemmantized_list = []

    for tag in tags:
      wordnet_tag = penn_to_wordnet(tag[1])
    
      if wordnet_tag != None:
          lemmantized_list.append( WordNetLemmatizer().lemmatize(tag[0],wordnet_tag) )
      else:
          lemmantized_list.append(tag[0])

    return lemmantized_list

def test_clean_text():
    test = "The quick brown\n fox was, running quickly through the yards."
    actual_text = text_clean(test)
    expected_text = ["quick", "brown", "fox", "run", "quickly", "yard"]
    unittest.TestCase.assertCountEqual(actual_text, expected_text)

# ---------------------------------------------------------------------------------
def text_tokenize(clean_text: list) -> dict:
    return dict(Counter(clean_text))


def test_text_tokenize():
    word_list = ["the", "the", "result", "testing", "testing", "testing"]
    actual = text_tokenize(word_list)
    expected = {"the": 2, "result": 1, "testing": 3}
    unittest.TestCase.assertDictEqual(actual, expected)


# ---------------------------------------------------------------------------------
def process_file(pdf_path: str):
    es = get_elastic_instance()
    #unprocessed_pdfs = filter_list(pdf_list)
    
    if not file_exists(pdf_path, es):
        # Get the text from the pdf
        pdf = read_pdf(pdf_path)

        # Clean out unwanted chars
        clean_text = text_clean(pdf.text)
        
        # Tokenize the output
        pdf.tokenized_words = text_tokenize(clean_text)
        print(len(pdf.tokenized_words))

        # Insert the file to elasticsearch
        insert_file(pdf, es)


if __name__=="__main__":
    from file_handling import read_pdf
    import operator
    import time

    start = time.time()
    
    full_text = read_pdf(r"C:\Users\datippett\Downloads\After_The_G_Zero_.pdf")
    read_time_end = time.time()
    print("Read PDF: ", read_time_end - start)

    tokenized_text = process_text(full_text)
    print(sorted(tokenized_text, key=tokenized_text.get, reverse=True)[:5])

    end = time.time()
    print("Parse Text: ", end - read_time_end)
    print("Total Time: ", end - start)
