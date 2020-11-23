from utilities.ntlk_import import *
import re

regex = re.compile('[^a-zA-Z]')
stop_words = set(stopwords.words('english'))

def text_clean(full_text: str) -> str:
    word_bag = full_text.split()

    for word in word_bag:
        tmp_word = word.lower()
        
        # Remove non-alpha
        tmp_word = regex.sub('', tmp_word)

        tmp_word = word_lemmantize(tmp_word)

        if not is_stopword(tmp_word):
            yield tmp_word


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


def word_lemmantize(word):
    tag = nltk.pos_tag(word_tokenize(word))
    wordnet_tag = penn_to_wordnet(tag[0][1])
    
    if wordnet_tag != None:
        return WordNetLemmatizer().lemmatize(tag[0][0],wordnet_tag)

    return word


def text_tokenize(full_text):
    pass


if __name__=="__main__":
    # Sample for testing
    phrase = "The quick brown\n fox was, running quickly through the yards."
    clean_text = text_clean(phrase)
    for word in clean_text:
        print(word)

# Sample output:
#
# The -> 
# quick -> quick
# brown\n -> brown
# fox -> fox
# was, -> 
# running -> run
# quickly -> quickly
# through -> 
# the -> 
# yards. -> yard
