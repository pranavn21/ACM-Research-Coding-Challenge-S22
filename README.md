# ACM Research Coding Challenge (Spring 2022)

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-S22`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uTpjeA8G).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#question-one)Question One

[Binary classification](https://en.wikipedia.org/wiki/Binary_classification) is a type of classification task that labels elements of a set (i.e. dataset) into two different groups. An example of this type of classification would be identifying if people had a specific disease or not based on certain health characteristics. The dataset found in `mushrooms.csv` holds data (22 different characteristics, specifically) about different types of mushrooms, including a mushroom's cap shape, cap surface texture, cap color, bruising, odor, and more. Remember to split the data into test and training sets (you can choose your own percent split). Information about the meaning of the letters under each column can be found within the file `attributelegend.txt`.

**With the file `mushrooms.csv`, use an algorithm of your choice to classify whether a mushroom is poisonous or edible.**

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library or API you want to implement this, just document which ones you used in this README file.** Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

-----

# Pranav Nair's Submission 

First, I read about binary classification on the wikipedia page. That led me to learning about linear regression in one of the source videos, since that was necessary in order ot perform binary classification using Python. I had to research on how to read and write to CSV files first. Once I was able to read the files properly, I used the source video to use the Panda and Scikit Learn libraries to use the input data that was provided. First, I had to take the CSV file and create a duplicate file using the Panda library, so that I could convert the chars into ASCII. I believe ASCII would work since each of the columns had a unique char (for that particular column, meaning that the same column/attributes would not have the same char more than once). This would help in the linear regression/machine learning phase. Once I had the duplicate CSV file with ASCII values, I used the Scikit's library to first split the data into test and training sets, as the instructions asked us to do so. I printed the amount of rows/columns in the training set, and the rows/column in the test set to give an idea of the proportions. Using the training set, I was able to create a line of best using the scikit's LogisticRegression tool. After that, I was able to find the score (mean accuracy), which would indicate the accuracy of predictions. Then, since my test set was already very large, I decided to only test 5 of those values since I wanted the output to be clean; although, that value can be changed to the maximum test values available (1625). 
I definitely learned a lot in this project, and it gave me a basic idea of machine learning (and data science). I learned about the Panda and Scikit library, csv files and how to use them in Python, and other minor details such as selecting particular indices in Python using ':". I think that my code was right, as I got a high accuracy, which I believe was intended from this project. 

# Sources

## C. Schafer, “Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files,” YouTube, 09-Aug-2017. [Online]. Available: https://www.youtube.com/watch?v=q5uM4VKywbA. [Accessed: 01-Feb-2022]. 
&emsp; This source helped me with basic CSV reading/writing. This was important as in order to proceed with linear regression, my files would need to be in numeric values. Therefore, I decided to convert all chars into ASCII values, and this source showed how to duplicate the input file, and edit every line on the new file.


## Dragonfly Statistics, “Scikit Learn : Binary Classification for the Pima Diabetes Data Set,” YouTube, 23-Nov-2017. [Online]. Available: https://www.youtube.com/watch?v=U1JIo8JSuYo. [Accessed: 31-Jan-2022].  
&emsp; This source was the primary source I used to understand how to use both the Panda data analysis library and sci-kit learn machine learning library. The source demonstrated how to use the Panda library to read the CSV input file, and then use the sci-kit library to split the dataset into two sets (training and testing). It also showed how to use sci-kit's logistic regression to perform binary classification, and then display the mean accuracy.


## jGraves, “Reply to: How to convert a list of characters to ASCII in python?,” Stack Overflow, 13-Nov-2017. [Online]. Available: https://stackoverflow.com/a/47272500. [Accessed: 31-Jan-2022]. 
&emsp; This source was used along with source 1 to convert the chars to ASCII. I needed this source to find a way to convert a list of chars into ASCII, and I found the map() function would be helpful, after referring to this source.