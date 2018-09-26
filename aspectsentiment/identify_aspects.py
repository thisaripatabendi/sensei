from identification import *
from nltk.sentiment import SentimentIntensityAnalyzer

from read_files import *

if __name__ == '__main__':
    review = input("Insert review : ")

    aspects = getAspects('../datastore/aspects.csv')

    parts = seperate(review)

    sid = SentimentIntensityAnalyzer()

    for part in parts:
        word_tokens = noiseClear(part)
        list_of_words = lemmetize(word_tokens)

        for word in list_of_words:
            for aspect in aspects:
                if word in aspect[1]:
                    ss = sid.polarity_scores(part)
                    score = ss['pos'] - ss['neg']
                    print(part)
                    print(aspect[0], " : ", score)
                    print()


