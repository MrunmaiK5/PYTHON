#######################################################################################
#   Function name   :   IsDivisible
#   Description     :   Checks whether given number is divisible by 5
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

IsDivisible = lambda No : (No%5 == 0)

def main():
    Ret = False
    Ret = IsDivisible(6)

    if Ret == True:
        print("It is dicisible")
    else:
        print("It is divisible")

if __name__ == "__main__":
    main()