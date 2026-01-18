#######################################################################################
#   Function name   :   LMin
#   Description     :   Returns minimum number from two given numbers
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

LMin = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Ret = 0
    Ret = LMin(6,1)

    print("Minimum :",Ret)

if __name__ == "__main__":
    main()