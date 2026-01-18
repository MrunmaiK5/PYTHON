#######################################################################################
#   Function name   :   Factors
#   Description     :   Displays factors of given number
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def Factors(No):
    for i in range(1,No+1):
        if No % i == 0:
            print(i)


def main():
    Ret = Factors(12)


if __name__ == "__main__":
    main()