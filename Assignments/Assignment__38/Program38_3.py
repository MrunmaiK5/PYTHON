import pandas as pd

########################################################################################################
#
#   Description     :   Loads dataset and display avarage study hours and attendance, maximum previous 
#                       score, and minimum sleep hours
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

# Average study hours
print("Average study hour is : ")
# print(df["StudyHours"].mean())
print( (df["StudyHours"].sum()) / len(df["StudyHours"]))
print(Border)

# Average attendance
print("Average attemdance is : ")
print( (df["Attendance"].sum()) / len(df["Attendance"]))
print(Border)

# Maximum previous score
print("Maximum previous score is : ")
print(df["PreviousScore"].max())
print(Border)

# Minimum sleep hours
print("Minimum sleep hours is : ")
print(df["SleepHours"].min())
print(Border)