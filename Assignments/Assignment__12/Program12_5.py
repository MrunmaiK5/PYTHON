#######################################################################################
#   Function name   :   ReverseNNumbers
#   Description     :   Displays reverse of n natural numbers
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def ReverseNNumbers(No):
    for i in range(No,0,-1):
        print(i)

def main():
    ReverseNNumbers(5)


if __name__ == "__main__":
    main()