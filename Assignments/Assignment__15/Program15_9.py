from functools import reduce

#######################################################################################
#   Function name   :   Product
#   Description     :   Returns product of numbers from given list of numbers
#   Input           :   List
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Product = lambda No1, No2 : No1 * No2 

def main():
    Ret = 0
    Data = [10,20,30,40,50]
    
    Ret = reduce(Product,Data)

    print("Product of numbers is :",Ret)

if __name__ == "__main__":
    main()