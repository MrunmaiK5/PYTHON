import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

###########################################################################################################
#
#   Description     :   Plotted a boxplot that shows distribution of attendance
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   02/03/26
#
###########################################################################################################

Border = "-"*40

# Load dataset

print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")

print(Border)

plt.figure(figsize=(8,5))
sns.scatterplot(data = df, x =df['AssignmentsCompleted'], y=df['Attendance'], hue='FinalResult')

plt.title("Scatter Plot")
plt.xlabel("Assignments completed")
plt.ylabel("Attendance")

plt.grid(True)
plt.show()