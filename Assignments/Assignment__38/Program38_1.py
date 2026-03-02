import pandas as pd

########################################################################################################
#
#   Description     :   Loads student_performance_ml.csv and display first and last 5 records, number 
#                       of rows and columns, list of columns and their data type
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   02/03/26
#
########################################################################################################

Border = "-"*40

# Load dataset

print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")

print(Border)
# First 5 records from dataset
print("First 5 records are :")
print(df.head())

print(Border)
# Last 5 records from dataset
print("Last 5 records are :")
print(df.tail())

print(Border)
# total rows and columns in data set
print("Total rows and columns are :")
print(df.shape)

print(Border)

# List of column names
print("Columns are :")
print(list(df.columns))

print(Border)

# data type of each column
print("Data type of each columns are :")
for i in list(df.columns):
    print(i," : ",type(i))

print(Border)