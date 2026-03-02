import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

########################################################################################################
#
#   Description     :   Plotted a histogram that shows the distribution of StudyHours among students
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

plt.figure(figsize=(8,5))
plt.hist(df['StudyHours'], color='skyblue',edgecolor="black")

plt.title("Histogram")

plt.grid(alpha=0.3)
plt.show()