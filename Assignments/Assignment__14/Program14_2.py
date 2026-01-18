#######################################################################################
#   Function name   :   LCube
#   Description     :   Returns cube of given number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

LCube = lambda No : (No*No*No)

def main():
    Ret = 0
    Ret = LCube(6)

    print("Cube :",Ret)

if __name__ == "__main__":
    main()