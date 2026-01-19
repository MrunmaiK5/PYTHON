from functools import reduce

#######################################################################################
#   Function name   :   Min
#   Description     :   Returns minimum of number from given list of numbers
#   Input           :   List
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Min = lambda No1, No2 : No1 if No1 < No2 else No2 

def main():
    Ret = 0
    Data = [10,20,30,40,50]
    
    Ret = reduce(Min,Data)

    print("Min number is :",Ret)

if __name__ == "__main__":
    main()