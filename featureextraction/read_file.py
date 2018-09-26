import csv

from short_forms import *

def readCSV(file):

    academic_rev = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for num, row in enumerate(reader):  # stop the count from 10

            # Replace appostrophe/short words
            sentence = decontracted(row['Review'])

            academic_rev.append(sentence)

            if (num >= 199):
                break

    return academic_rev


def readTestCSV(file, column):
    academic_rev = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for num, row in enumerate(reader):  # stop the count from 10

            # Replace appostrophe/short words
            sentence = decontracted(row[column])

            academic_rev.append(sentence)

            if (num >= 199):
                break

    return academic_rev