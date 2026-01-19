#######################################################################################
#   Function name   :   EvenNo
#   Description     :   Returns list of even numbers from given list of numbers
#   Input           :   List
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

EvenNo = lambda No : (No%2 == 0)

def main():
    Ret = 0
    Data = [11,20,34,55,101,200]
    
    Ret = list(filter(EvenNo,Data))
    print("Even numbers are :",Ret)

if __name__ == "__main__":
    main()