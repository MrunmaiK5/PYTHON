#######################################################################################
#   Function name   :   LMax
#   Description     :   Returns maximum number from two given numbers
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

LMax = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Ret = 0
    Ret = LMax(6,1)

    print("Maximum :",Ret)

if __name__ == "__main__":
    main()