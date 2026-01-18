#######################################################################################
#   Function name   :   tableX
#   Description     :   Displays table of a given number 
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def tableX(a):
    for i in range(1,11):
        print(a*i)

def main():
    tableX(5)

if __name__ == "__main__":
    main()