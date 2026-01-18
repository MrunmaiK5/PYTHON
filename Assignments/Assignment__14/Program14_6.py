#######################################################################################
#   Function name   :   IsOdd
#   Description     :   Checks whether given number is odd or not
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

IsOdd = lambda No : (No%2 != 0)

def main():
    Ret = False
    Ret = IsOdd(6)

    if Ret == True:
        print("It is odd")
    else:
        print("It is even")

if __name__ == "__main__":
    main()