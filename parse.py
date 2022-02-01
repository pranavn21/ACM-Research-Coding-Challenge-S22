# Pranav Nair
# This is for the Coding Assignment for my ACM Research Application
# January 31, 2022

import csv
import os

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

lr = LogisticRegression(max_iter=9000) # Making sure to set max iterations to atleast 9000, since the number of lines in mushrooms.csv was 8000+

svc = LinearSVC(C=1.0) # Not changing C value, as the source instructed to

df = pd.read_csv('mushrooms.csv',index_col=0) # Read the mushroom.csv file
df.iloc[:0, :].to_csv("copy_of_mushrooms.csv") # ONLY copy and paste the first line into a new file called copy_of_mushrooms.csv

with open ('mushrooms.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip first row

    with open ('copy_of_mushrooms.csv', 'a') as new_file: # a for append, as we don't want to overwrite the first line
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            ascii_values = map(ord, line) # Using the map function to convert all chars in the line to ASCII
            csv_writer.writerow(list(ascii_values)) # Write the new ASCII line in the copy csv

###

mushrooms = pd.read_csv('copy_of_mushrooms.csv')

train, test = train_test_split(mushrooms, test_size = 0.2) # This is to split our data set into two sets: Train data and Test data
print("We will be training with " + str(train.shape[0]) + " rows (" + str(train.shape[1]) + " columns)")
print("We will be testing with " + str(test.shape[0]) + " rows (" + str(train.shape[1]) + " columns)")

train_feat = train.iloc[:,1:23] 
train_targ = train["class"]

lr.fit(train_feat, train_targ) # Fit the model
print("After our binary classification using linear regression, the score (mean accuracy) was " + str(lr.score(train_feat, train_targ)))
print("This means that using self.predict(X) will result in accuracy of " + str(lr.score(train_feat, train_targ)*100) + "%")

test_feat = train.iloc[:,1:23] 
test_targ = train["class"]
print("PREDICTIONS OF 5 INPUTS:") # Here we can test some predictions by testing 5 inputs
print(lr.predict(test_feat[0:5]))
print("ACTUAL VALUE OF 5 INPUTS:") # We will also print the actual values to compare
print(test_targ.iloc[0:5].array)

os.remove('copy_of_mushrooms.csv') # Remove the no longer needed file

