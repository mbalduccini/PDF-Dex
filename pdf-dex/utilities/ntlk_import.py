import nltk
import importlib

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords

need_reload = False

# NLTK needs data downloaded so this checks if it exists
#   if it doesnt exist it will download it and reload
try:
  nltk.data.find('punkt')
except LookupError:
  nltk.download('punkt')
  need_reload = True

try:
  nltk.data.find('averaged_perceptron_tagger')
except LookupError:
  nltk.download('averaged_perceptron_tagger')
  need_reload = True

try:
  nltk.data.find('wordnet')
except LookupError:
  nltk.download('wordnet')
  need_reload = True

try:
  nltk.data.find('stopwords')
except LookupError:
  nltk.download('stopwords')
  need_reload = True

if need_reload:
  importlib.reload(nltk)

