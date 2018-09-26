from nltk.sentiment import SentimentIntensityAnalyzer
from short_forms import *
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn, stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer

from nltk.corpus import wordnet as wn



def seperate(review):
    # sample = re.split(r' *[\.\?!][\'"\)\]]* *', sentence)
    # sample = re.split(r'[.,&]', sentence)
    # sample = re.sub(r'(and|\.|but|,)', r'\1\n', review).split('\n')

    sample = re.sub(r'(\.|but)', r'\1\n', review).split('\n')

    # (? < !\w\.\w.)(? < ![A - Z][a - z]\.)(? <= \.| \?)\s

    return sample

def noiseClear (sentence):

    # tokenize the sentence
    tokens = tokenize(sentence)

    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]

    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    # print(words[:100])
    return words


def lemmetize (word_tokens):

    list_of_words = []
    lmtzr = WordNetLemmatizer()

    for word in word_tokens:
        tokenized = nltk.tag.pos_tag([word])
        type = tokenized[0]

        # verbs in to present simple format
        if type[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            list_of_words.append(WordNetLemmatizer().lemmatize(word, 'v'))
        else:
            #plurel -> singular
            list_of_words.append(lmtzr.lemmatize(word))

    return list_of_words

def tokenize(sentence):

    # split into words
    tokens = word_tokenize(sentence)

    # convert to lower case
    tokens = [w.lower() for w in tokens]

    return tokens