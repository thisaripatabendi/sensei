from nltk.corpus import wordnet as wn, stopwords
from nltk.stem.wordnet import WordNetLemmatizer


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

    return synonyms


if __name__ == '__main__':
    wordlist = ['help', 'time', 'feedback', 'understand', 'grader', 'assignment']

    for word in wordlist:
        syn = getSynonymes(word)
        # v = verbify(word)
        print(word, " - ", syn)



    list_of_words = []
    lmtzr = WordNetLemmatizer()

    # # test lemmatize
    # print('grading - ', (lmtzr.lemmatize('grades')))
    # word = 'supervising'
    # print (word + "-->" + WordNetLemmatizer().lemmatize(word, 'v'))\




