#######################################################################################
#   Function name   :   Largest
#   Description     :   Returns largest of three numbers
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Largest = lambda No1, No2, No3 : No1 if No1>No2 and No1>No3 else (No2 if No2>no1 and No2>No3 else No3)  

def main():
    Ret = 0
    Ret = Largest(6,4,2)

    print("Largest is :",Ret)

if __name__ == "__main__":
    main()