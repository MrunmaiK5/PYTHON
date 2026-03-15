import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

###########################################################################################################
#
#   Description     :   Build and trained a model and calculated it's accuracy using accuracy_score method
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

# Splitting variables

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

X= df[feature_cols]
Y = df["FinalResult"]

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

# Model Building

Model = DecisionTreeClassifier()

# Training model

Model.fit(x_train,y_train)

# Testing model

y_pred = Model.predict(x_test)

print("Actual values : ")
print(y_test)

print("Predicted values : ")
print(y_pred)

# Evaluate model performance

Result = accuracy_score(y_test, y_pred)
print("Accuracy of model is: ",(Result*100))