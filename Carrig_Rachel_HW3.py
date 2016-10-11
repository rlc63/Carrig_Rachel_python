# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:11:22 2016

@author: ibrlouise
"""
#Overall Comment: Good exercise. You can save the data or table you read in so that you don't need to read in every time.

"""
first, we import the information as a table into python from a local path
"""
import pandas #we first import pandas so that we can use all the functions that come from it
pandas.read_table("/Users/ibrlouise/Documents/Grad School - Fall 2016/510/Homework/bezdekIris.data", 
                  header=0, sep=',')
#the function above reads the table in our local document. it uses the first row (row 0) as the header, 
#and uses commas to separate the columns (since that is how the data is structured)

"""
we want to display the first 10 and last 10 rows:
"""
pandas.read_table("/Users/ibrlouise/Documents/Grad School - Fall 2016/510/Homework/bezdekIris.data", 
                  header=0, sep=',', skiprows=range(11, 141))
#Comment:Actually you can save the data or table you read in to one data frame. And do operations based on this.

#in this function, we use the skiprows command to skip the range of rows 11 to 141, leaving us with the 
#first ten and the last ten rows

"""
next, we want to print simple location statistics (Count, Mean, STD, Min, 25%, 50%, 75%, MAX)
"""
#we first give a name to the table we created earlier with all data points.  we will call it dataset.
#we will use this name for the rest of the assignment
dataset = pandas.read_table("/Users/ibrlouise/Documents/Grad School - Fall 2016/510/Homework/bezdekIris.data", 
                  header=0, sep=',')
dataset.describe(percentiles=None, include=None, exclude=None)
#dataset.describe calls the function describe to our defined dataset.  describe prints the count, mean, 
#STD, min, ma, 25%, 50%, and 75% for our numerical variables

"""
finally, we want to create a histogram for the numerical columns and a bar chart for the nominal column
"""
#using the earlier defined dataset, we are able to create a histogram of the numerical data
dataset.hist(column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False, figsize=None, layout=None, bins=10)

#next, we will create a bar chart for the nominal column
dataset.irisclass.value_counts().plot(kind='bar')
#NOTE: we changed the name of the class column to be irisclass, since python recognizes class as a function.
#we call the dataset that we created from the information earlier, and then specifically the column
#irisclass that we want to use to make the bar chart.  we count the number of times each item appears
#in that column from the value_counts() command. lastly, we use plot to create the graph, which we specify
#to be a bar graph.
