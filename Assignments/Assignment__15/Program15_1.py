#######################################################################################
#   Function name   :   Square
#   Description     :   Returns list of squares
#   Input           :   List
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Square = lambda No : No*No

def main():
    Ret = 0
    Data = [10,20,30,40,50]
    
    Ret = list(map(Square,Data))
    print("Square is :",Ret)

if __name__ == "__main__":
    main()