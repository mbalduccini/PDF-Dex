from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import nltk

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

import re

regex = re.compile('[^a-zA-Z]')

def text_clean(full_text: str) -> str:
    word_bag = full_text.split()

    for word in word_bag:
        tmp_word = word.lower()
        
        # Remove non-alpha
        tmp_word = regex.sub('', tmp_word)

        tmp_word = word_lemmantize(tmp_word)
        yield tmp_word


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    else:
        return None

def word_lemmantize(word):
    tag = nltk.pos_tag(word_tokenize(word))
    wn_tag = penn_to_wn(tag[0][1])
    
    if wn_tag != None:
        return WordNetLemmatizer().lemmatize(tag[0],wn_tag)

    return word

def text_tokenize(full_text):
    pass

if __name__=="__main__":
    phrase = "The quick brown\n fox was, running quickly through the yards"
    clean_text = text_clean(phrase)
    for word in clean_text:
        print(word)