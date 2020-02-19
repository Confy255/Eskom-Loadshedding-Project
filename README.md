# Group3 analyse predict
The project has 7 functions which analyse Eskom data which is passed to each function.

*Function takes in a list integers one calculates metrics of a given data given as a list and outputs the metrics (mean, median,maximum,minimum,standard deviation, variance) as a dictionary.
*Function two takes in a list of integers then returns a five number summary (median,maximum,minimum,q1,q3)
*Function three takes in a date as string in one format and convert it to anonther string format
*Function four takes in a dataframe and returns a new dataframe with an added column of extracted hashtags and another column of municipality mentioned in each tweets.
*Function five accepts a given dataframe and returns a new dataframe that has a number of tweets per day.
*Function six takes in a dataframe and output a new dataframe with an added column that split a sentence to a list of indivisual words.
*Function seven takes in a data frame and output a new data frame with an added column of the tweets without stop words.


# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites
You need to install python with Anaconda

# Installing
Navigate to https://repo.continuum.io/archive/
Select the appropriate version for your machine (windows 32bit or 64bit)
Download the latest version for Anaconda

# Deployment
You need to install the module for the function.
On your computer search for Anaconda prompts.
Do a pip install with the following comand: 'pip install git+https://github.com/Confy255/group3predict.git' 
To import the module to your Jupyter notebook type the following comand inside your cell
from group3predict import ourmodule
To call any function inside the module you need to type the following command
ourmodule.functionname(parameter)

# Authors
Sandile Mkize,
Sandile Dladla,
Confidence Ledwaba,
Karabo Leso,
Evans Marema

# License
This project is licensed under the MIT License - see the LICENSE.md file for details