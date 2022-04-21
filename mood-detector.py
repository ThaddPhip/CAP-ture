


#make the threshold_calc just a function file that reads sample data and determines thresholds
#then make this a main file for the emotional assessment of any data from that person in the future
#by calling the results from this file
#when the main file determines a mood save that indication to a separate file in python that displays/saves vids and quotes
#code for threshold calc:
from csv import reader
# open file in read mode
with open('thaddeaus_happy.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)

#find columns we need to assess
#Cut off first x secs (rows) and last x secs (rows)- you can also do this in for loop like for col=x:col=x
#filter out the blinks w a logic statement of if there is a value in the Beta_TP10 column
#like for example total=0 for row=row+1 if row 'Beta_TP10'==0 then row += 1 else total=total+row
# -add that row of alpha tp9 to a total then div that total by the sum of its rows for avg
#use averages as thresholds, we could see how many rows we'd need to consider for diff patients/genders/etc
#maybe diff starting threshold based on female or male option button


#then for each new patient we do clinical trial of diff moods and find their thresholds to use for future data


#extra code
#import csv
#filename = "thaddeaus_happy.csv"
# opening the CSV file
#with open(filename, mode='r') as file:
    # reading the CSV file
 #   csvFile = csv.reader(file)
    # displaying the contents of the CSV file
   # filename['Theta_TP9'].mean()

#import pandas as pd
#data = pd.read_csv('thaddeaus_happy.csv')
#data['Theta_TP9']


#import csv
#csv_file = csv.reader(open("thaddeaus_happy.csv"))

#dist = 0
#for row in csv_file:
 #   _dist = row[2]
 #   try:
 #       _dist = float(_dist)
 #   except ValueError:
 #       _dist = 0
#
 #   dist += _dist