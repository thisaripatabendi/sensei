from nltk.sentiment import SentimentIntensityAnalyzer

from read_file import *
from overall_calculation import *

if __name__ == '__main__':

    # read CSV file
    print("Reading the csv file .....", '\n')

    lec1 = readTestCSV('../datastore/testdata1.csv', 'Lecturer 01')
    calculate('Lecturer 06', lec1)
    lec2 = readTestCSV('../datastore/testdata1.csv', 'Lecturer 02')
    calculate('Lecturer 03', lec2)
    lec3 = readTestCSV('../datastore/testdata1.csv', 'Lecturer 03')
    calculate('Lectirer 04', lec3)