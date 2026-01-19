#######################################################################################
#   Function name   :   EvenCount
#   Description     :   Returns count of even numbers from given list of numbers
#   Input           :   List
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Product = lambda No : (No%2 == 0)

def main():
    Ret = 0
    Count = 0
    Data = [10,15,20,33,40,55]
    
    Ret = list(filter(Product,Data))

    Count = len(Ret)

    print("Count of even numbers is :",Count)

if __name__ == "__main__":
    main()