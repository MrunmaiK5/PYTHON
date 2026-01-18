#######################################################################################
#   Function name   :   SumOfNNumbers
#   Description     :   Displays summation of first n natural numbers
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def SumOfNNumbers(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    print(sum)

def main():
    SumOfNNumbers(5)

if __name__ == "__main__":
    main()