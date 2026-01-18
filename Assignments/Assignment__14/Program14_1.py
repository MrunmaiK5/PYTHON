#######################################################################################
#   Function name   :   LSquare
#   Description     :   Returns square of given number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

LSquare = lambda No : (No*No)

def main():
    Ret = 0
    Ret = LSquare(6)

    print("Square :",Ret)

if __name__ == "__main__":
    main()