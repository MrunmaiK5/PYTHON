import pandas as pd

########################################################################################################
#
#   Description     :   Loads dataset and display total number of passed and failed students
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

# total number of students
print("Total number of students are : ")
print(df.shape[0])
#len(df)
print(Border)

# number of students passed
print("Total number of passed student : ")
print(df["FinalResult"].sum())
print(Border)

# number of students failed
print("Total number of failed student : ")
print((df["FinalResult"] == 0).sum())
print(Border)