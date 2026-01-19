#######################################################################################
#   Function name   :   StringLen
#   Description     :   Returns list of strings whose length are greater than 5
#   Input           :   List
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

Divisible = lambda No : ((No%3 == 0) and (No%5==0))

def main():
    Ret = list()
    Data = [10,20,30,40,50,60,15]
    
    Ret = list(filter(Divisible,Data))

    print("Numbers divisible by 3 and 5 are :",Ret)

if __name__ == "__main__":
    main()