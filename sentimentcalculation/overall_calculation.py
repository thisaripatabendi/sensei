from nltk.sentiment import SentimentIntensityAnalyzer


def calculate(lecname, academic_rev):
    num = len(academic_rev)

    sid = SentimentIntensityAnalyzer()
    compounds = 0

    for rev in academic_rev:
        ss = sid.polarity_scores(rev)
        compounds = compounds + ss['compound']
        # print(rev)
        # print(ss)
        # print()

    average = compounds*100/num
    print(lecname, " : " , str(round(average, 2)))


    # print("number of reviews : " , num)
    print()