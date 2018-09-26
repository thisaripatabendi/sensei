import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn, stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer
import csv


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


def twoWordPairs(words):

    # will be a list of lists
    pairs = list()

    # iterate from 0 up to the length of the list minus one (so we don't
    # inadvertently grab elements from beyond the length of the list)
    for i in range(len(words) - 1):
        pair = words[i:i + 2]  # i.e., the element at i and the next element
        pairs.append(pair)

        # print out pairs
        # for pair in pairs:
        #     print(' '.join(pair))

    return pairs


def createFile (filename):
    # create a csv file
    filewords = csv.writer(open(filename, 'w', newline=''))  # newline='' -> to remove empty line between each row

    return filewords


def tokenize(sentence):

    # split into words
    tokens = word_tokenize(sentence)

    # convert to lower case
    tokens = [w.lower() for w in tokens]

    return tokens