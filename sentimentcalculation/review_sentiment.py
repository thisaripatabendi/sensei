from nltk.sentiment import SentimentIntensityAnalyzer


if __name__ == '__main__':
    sentence = input('Enter the review : ')

    sid = SentimentIntensityAnalyzer()

    ss = sid.polarity_scores(sentence)

    score = ss['pos'] - ss['neg']
    print(sentence)
    print(ss)
    print(score)