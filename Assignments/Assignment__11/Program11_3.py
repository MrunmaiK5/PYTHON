#######################################################################################
#   Function name   :   SumOfDigits
#   Description     :   Displays summation of digits of a number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def SumOfDigits(a):
    Sum = 0
    Digit = 0
    while a > 0:
        Digit = a % 10
        Sum =int(Digit + Sum) 
        a = a / 10

    return Sum


def main():
    Ret = SumOfDigits(123)
    print("Sum of digits is :",Ret)

if __name__ == "__main__":
    main()