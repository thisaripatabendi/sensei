from read_file import *
from Formatting import *
from Feature import *


if __name__ == '__main__':

    academic_rev = readCSV("../datastore/dataset.csv")
    print(len(academic_rev))


    features = []

    # extrac nouns
    for sentence in academic_rev:
        # noise clear
        word_tokens = noiseClear(sentence)
        # print(word_tokens, '\n')

        list_of_words = lemmetize(word_tokens)

        # break into word pairs
        word_pairs = twoWordPairs(list_of_words)

        # check for nouns
        features_of_one = extractFeatures(word_pairs)
        features = features + features_of_one

    # get most frequent nouns
    most_frequent_nouns = getMostFrequent(features, 'frequent.csv')

    # check for sysnonymes remove from most frequent list
    synonymes_removed_list = removeSynonymes(most_frequent_nouns)

    most_frequent = getMostFrequentWOrds(synonymes_removed_list, 20)
    filewords = createFile('../datastore/features.csv')

    for key, count in most_frequent:
        # filewords = createFile('frequentNouns.csv')
        filewords.writerow([key, count])
