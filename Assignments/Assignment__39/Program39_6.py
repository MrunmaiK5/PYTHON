import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

###########################################################################################################
#
#   Description     :   Build and trained a model and calculated it's training and testing accuracy
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   10/03/26
#
###########################################################################################################

Border = "-"*40

# Load dataset

print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")

print(Border)

# Splitting variables

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]
print(Border)
X= df[feature_cols]
Y = df["FinalResult"]

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

print("x_train : ",x_train.shape)
print("x_test : ",x_test.shape)
print("y_train : ",y_train.shape)
print("y_test : ",y_test.shape)
print(Border)

# Model1 Building

Model1 = DecisionTreeClassifier(max_depth=1)
Model2 = DecisionTreeClassifier(max_depth=2)
Model3 = DecisionTreeClassifier(max_depth=3)

# Training model

Model1.fit(x_train,y_train)
Model2.fit(x_train,y_train)
Model3.fit(x_train,y_train)

# Testing model

y_pred1 = Model1.predict(x_test)
y_pred2 = Model2.predict(x_test)
y_pred3 = Model3.predict(x_test)

# Evaluate model performance
print(Border)

Result1 = accuracy_score(y_test, y_pred1)
print("Accuracy of model1 is: ",(Result1*100))

Result2 = accuracy_score(y_test, y_pred2)
print("Accuracy of model2 is: ",(Result2*100))

Result3 = accuracy_score(y_test, y_pred3)
print("Accuracy of model3 is: ",(Result3*100))

print(Border)


print(Border)