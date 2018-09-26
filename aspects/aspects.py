from nltk.corpus import wordnet as wn, stopwords
from nltk.stem.wordnet import WordNetLemmatizer

from Formatting import *

def getSynonymes(word):

    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    if word == 'assignment':
        synonyms.append('coursework')
        synonyms.append('question')
        synonyms.append('test')

    if word == 'grader':
        synonyms.append('mark')
        synonyms.append('grade')

    if word == 'feedback':
        synonyms.append('supervisor')
        synonyms.append('supervise')

    return synonyms


if __name__ == '__main__':
    wordlist = ['help', 'time', 'feedback', 'understand', 'grader', 'assignment']

    filewords = createFile('../datastore/aspects.csv')
    filewords.writerow(['word', 'synonym'])

    for word in wordlist:
        syn = getSynonymes(word)
        # v = verbify(word)
        print(word, " - ", syn)
        filewords.writerow([word, syn])

    #
    # print(getSynonymes('supervision'))








