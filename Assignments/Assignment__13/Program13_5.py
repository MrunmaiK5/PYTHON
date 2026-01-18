#######################################################################################
#   Function name   :   DisplayGrade
#   Description     :   Displays grade according to given marks
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   18/01/26
#######################################################################################

def DisplayGrade(No):
    if No >= 75:
        print("Distinction")
    elif No >= 60 and No < 75:
        print("First class")
    elif No >= 50 and No < 60:
        print("Second class")
    elif No < 50:
        print("Fail")
    else:
        print("Enter correct marks")

def main():
    DisplayGrade(80)

if __name__ == "__main__":
    main()