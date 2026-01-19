from functools import reduce

#######################################################################################
#   Function name   :   Add
#   Description     :   Returns addition of numbers from given list of numbers
#   Input           :   List
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Add = lambda No1, No2 : No1 + No2

def main():
    Ret = 0
    Data = [10,20,30,40,50]
    
    Ret = reduce(Add,Data)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()