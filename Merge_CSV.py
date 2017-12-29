import pandas as pd
import glob, os
import operator
import csv


os.chdir("Results/")
results = pd.DataFrame([])

for counter, file in enumerate(glob.glob("Results_*")):
    namedf = pd.read_csv(file, skiprows=0, usecols=[1, 2, 3, 4, 5, 6])
    results = results.append(namedf)

results.to_csv('combinedfile.csv')


reader = csv.reader(open("combinedfile.csv"), delimiter=",")

sortedlist = sorted(reader, key=operator.itemgetter(1))#, reverse=True)