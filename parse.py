import csv

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

lr = LogisticRegression(max_iter=9000)

svc = LinearSVC(C=1.0)
rfc = RandomForestClassifier(n_estimators=100)


df = pd.read_csv('mushrooms.csv',index_col=0)
df.iloc[:0, :].to_csv("copy_of_mushrooms.csv")
#df.to_csv('copy_of_mushrooms.csv')
with open ('mushrooms.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip first row

    with open ('copy_of_mushrooms.csv', 'a') as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            ascii_values = map(ord, line)
            csv_writer.writerow(list(ascii_values))

###

mushrooms = pd.read_csv('copy_of_mushrooms.csv')
mushrooms = mushrooms.apply(pd.to_numeric)

train, test = train_test_split(mushrooms, test_size = 0.2) # This is to split our data set into two sets: Train data and Test data
print("We will be training with " + str(train.shape[0]) + " rows (" + str(train.shape[1]) + " columns)")
print("We will be testing with " + str(test.shape[0]) + " rows (" + str(train.shape[1]) + " columns)")

train_feat = train.iloc[:,1:23] #train.iloc[:,1:23]
train_targ = train["class"]

#print(train_feat)
#print(str(train_feat.shape))
#print(str(train_targ.shape))

lr.fit(train_feat, train_targ) # Fit the model
print("After our binary classification using linear regression, the score (mean accuracy) was " + str(lr.score(train_feat, train_targ)))
print("This means that using self.predict(X) will result in accuracy of " + str(lr.score(train_feat, train_targ)*100) + "%")

#with open('mushrooms.csv','r') as csv_file: # Open up the CSV file, and save it to csv_file
 #       csv_reader = csv.reader(csv_file) # Read the CSV file we just got

  #      next(csv_reader) # Skip the first 

   #     for line in csv_reader:
    #        print(line[0])

