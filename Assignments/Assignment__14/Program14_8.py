#######################################################################################
#   Function name   :   Add
#   Description     :   Returns addition of two numbers
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Add = lambda No1, No2 : (No1 + No2)

def main():
    Ret = 0
    Ret = Add(6,4)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()