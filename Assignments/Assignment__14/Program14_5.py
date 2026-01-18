#######################################################################################
#   Function name   :   IsEven
#   Description     :   Checks whether given number is even or not
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

IsEven = lambda No : (No%2 == 0)

def main():
    Ret = False
    Ret = IsEven(6)

    if Ret == True:
        print("It is even")
    else:
        print("It is odd")

if __name__ == "__main__":
    main()