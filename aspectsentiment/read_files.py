import csv
from short_forms import *

def getAspects(file):

    aspects = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # stop the count from 10

            # Replace appostrophe/short words
            aspect = row['word']
            synonymes = row['synonym']
            tup = (aspect,synonymes)
            aspects.append(tup)

    return aspects


