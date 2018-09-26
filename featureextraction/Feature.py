import nltk
from collections import Counter

from Formatting import *
from synonymes import *

def extractFeatures (pairs):

    features = []

    for pair in pairs:
        firstword = nltk.tag.pos_tag([pair[0]])
        secondword = nltk.tag.pos_tag([pair[1]])
        # # adjective noun
        # ----------------------------- HIGH ADJECTIVE COUNT ALGORITHM ----------------------------------------
        # for i, j in firstword:
        #     if j in ['JJ', 'JJR', 'JJR']:
        #         for l, m in secondword:
        #             if m in ['NN', 'NNS', 'NNP', 'NNPS']:
        #                 features.append(l)
        #
        # # verb noun
        # for i, j in firstword:
        #     if j in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
        #         for l, m in secondword:
        #             if m in ['NN', 'NNS', 'NNP', 'NNPS']:
        #                 features.append(l)
        #
        # # noun noun
        # for i, j in firstword:
        #     if j in ['NN', 'NNS', 'NNP', 'NNPS']:
        #         for l, m in secondword:
        #             if m in ['NN', 'NNS', 'NNP', 'NNPS']:
        #                 feature_word = i + " " + l
        #                 features.append(l)
        #                 features.append(i)
        for i, j in secondword:
            #check second word a noun
            if j in ['NN', 'NNS', 'NNP', 'NNPS']:
                for l, m in firstword :
                    #if m in ['JJ', 'JJR', 'JJR', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                    #if m in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                    #check first word an adjective
                    if m in ['JJ', 'JJR', 'JJS']:
                        features.append(i)
                        # feature_word = l + " " + i
                        # features.append(feature_word)
                    # if m in ['NN', 'NNS', 'NNP', 'NNPS']:
                    #     features.append(i)
                    #     features.append(l)
                    #     # feature_word = l + " " + i
                    #     # features.append(feature_word)

    return features


def getMostFrequent(features, filename):

    mostfre = []

    # add most frequent words to a csv file
    # frequency = Counter(features)
    # most_frequent = frequency.most_common(200)  # first 10 words with the most frequency
    most_frequent = getMostFrequentWOrds(features, 200)
    filewords = createFile(filename)

    for key, count in most_frequent:
        # filewords = createFile('frequentNouns.csv')
        filewords.writerow([key, count])

        # add to mostfre list
        tup = (key, count)
        mostfre.append(tup)

    print ("---------- Most frequent 20 nouns ----------", '\n', mostfre, '\n')
    return mostfre


def getMostFrequentWOrds(list, number):

    frequency = Counter(list)
    most_frequent = frequency.most_common(number)

    return most_frequent


def removeSynonymes (mostfre):

    newlist = []
    new_list_with_synonyms = []

    # check sysnonyms
    for freword in mostfre:

        synonyms = getSynonymes(freword[0])

        frequency = freword[1]
        for tuple in mostfre:
            if (tuple[0] in synonyms and tuple[0] != freword[0]) or \
                    (tuple[0].find(freword[0]) != -1 and tuple[0] != freword[0]):
                frequency = frequency + tuple[1]
                mostfre.remove(tuple)

        newtuple = (freword[0], frequency)
        newlist.append(newtuple)
        new_list_with_synonyms.append(freword[0])

        if freword[0] not in new_list_with_synonyms:
            newlist.append(freword)
            new_list_with_synonyms.append(freword[0])

    return newlist
