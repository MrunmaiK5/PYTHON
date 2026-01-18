#######################################################################################
#   Function name   :   Divisible
#   Description     :   Checks whether given number is divisible by 5 and 2
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def Divisible(a):
    if (a%3 == 0) and (a%5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible")


def main():
    Divisible(15)

if __name__ == "__main__":
    main()