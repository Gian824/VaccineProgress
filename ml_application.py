# -*- coding: utf-8 -*-
"""ML Application.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDSCK2JxfLS33raVd94nhBkzSLrP6NWE

#Created By: Gianfranco Gonzales
##Source/Data Used: https://www.kaggle.com/gpreda/covid-world-vaccination-progress

#Main Idea#
Using the dataset provided from (https://www.kaggle.com/gpreda/covid-world-vaccination-progress), be able to find how many vaccinations/vaccines are available in each country and identify which countries require assistance with COVID-19 vaccine distribution. Use Github link in order to get updates from the dataset.

Github csv link: https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/vaccinations.csv


##Implementation#
Use linear regression modeling to separate countries and label as to whether they are above or below the world wide average for the vaccines to vaccinations ratio. We use linear regression to create a line of prediction, whith which we can use to determine if a country requires assistance based on whether or not they require assistance in the distribution of vaccines.

###Features
In this project, I used a dataset that is continuously updated (daily). With this I decided to obtain the dataset directly to the github repository to stay constantly up to date, rather than to download the dataset directly. As well, I have based the project around the fact that there may be new data about new countries in the future, and so attempted to keep the code flexible with added data such as creating a variable to read the number of countries (rows) in the dataset if more countries were to be added in the future.
"""

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

# import datasets
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
pre_vaccines = pd.read_csv(url)
# vaccines = vaccines.drop(vaccines[vaccines.total_vaccinations.isna()].index)

# In the dataset, there are many coppies of Countries with data recorded from different dates.
# I need to get rid of these duplicates in order to gain accurate data.

vaccines = pre_vaccines.groupby(["location",'iso_code'])['total_vaccinations','people_vaccinated','people_fully_vaccinated','daily_vaccinations_raw',
                                           'daily_vaccinations','total_vaccinations_per_hundred','people_vaccinated_per_hundred',
                                           "people_fully_vaccinated_per_hundred",'daily_vaccinations_per_million'].max().reset_index()
pd.reset_option('all')
display(vaccines)

# There's alot of data that show's up with NaN. In order to counter this, I need to converet all missing data into 0.
# I also converted many of the categories into integers to simplify calculations.
def show_raw():
  vaccines.fillna(value = 0, inplace = True)
  vaccines.total_vaccinations = vaccines.total_vaccinations.astype(int)
  vaccines.people_vaccinated = vaccines.people_vaccinated.astype(int)
  vaccines.people_fully_vaccinated = vaccines.people_fully_vaccinated.astype(int)

  vaccines.daily_vaccinations_raw = vaccines.daily_vaccinations_raw.astype(int)
  vaccines.daily_vaccinations = vaccines.daily_vaccinations.astype(int)
  vaccines.total_vaccinations_per_hundred = vaccines.total_vaccinations_per_hundred.astype(int)

  vaccines.people_fully_vaccinated_per_hundred = vaccines.people_fully_vaccinated_per_hundred.astype(int)
  vaccines.daily_vaccinations_per_million = vaccines.daily_vaccinations_per_million.astype(int)
  vaccines.people_vaccinated_per_hundred = vaccines.people_vaccinated_per_hundred.astype(int)

# At the end of the list includes the summary of the entire world that is not needed so I removed it.
  n = 2
  vaccines.drop(vaccines.tail(n).index, 
        inplace = True)

  display(vaccines)
  print ("working")
show_raw()

# Created X, Y variable to host portion of datasets
X = vaccines.total_vaccinations.values.reshape(-1, 1)
Y = vaccines.people_vaccinated.values.reshape(-1, 1)

# This is an example of the data in a plot without a linear regression line
plt.scatter(X, Y, color='blue')
plt.title('Total Vaccinations vs. People Vaccincated')
plt.xlabel('Total Vaccinations (In 10 Million)')
plt.ylabel('People Vaccinated (In 10 Million)')

plt.figure(figsize=(100,90))
plt.show

# Begining of Code for Linear Regression Model
def model():
  reg = LinearRegression()
  reg.fit(X, Y)
  Y_pred = reg.predict(X)

  plt.scatter(X, Y, color='blue')
  plt.plot(X, Y_pred, color='red')
  plt.title('Total Vaccinations vs. People Vaccincated')
  plt.xlabel('Total Vaccinations (In 10 Million)')
  plt.ylabel('People Vaccinated (In 10 Million)')

  plt.figure(figsize=(100,90))
  plt.show()
model()

# With this we can see the trend line for the linear regression model. 
# This allowes us to achieve our goal of separating, plus it allows us to predict 
# the trend to the total vaccinations versus the number of people vaccinated

# String used to assign Yes or No for the country's need of assistance
string = []
for i in range(len(vaccines)):
  string.append("")

for i in range(len(vaccines)):
  #if Y_pred[i] == 0:
    #Y_pred[i] += 1
  divide = X[i] / Y[i]
  Regression = X[i] / Y_pred[i]
#  print(Y[i])
#  print(' ')
#  print(Y_pred[i])

# Determination of whether the country requires assistance or not
  if math.inf > divide >= Regression:
    string[i] = 'No'
  elif divide < Regression:
    string[i] = 'Yes'
  else:
    string[i] = 'Yes'

# Final variable final included a list of the countries with their final verdict of whether or not the require assistance 
# with the distribution of the COVID vaccine

print("Countries that Require Assistance With Vaccine")
final = [0]*(len(vaccines))

i = 0
while i < len(final):
    final[i] = vaccines.iso_code[i], vaccines.location[i], string[i]
    i += 1
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.DataFrame(final, columns=["ISO", "Country", "Assistance Needed?"])

"""#END#"""

