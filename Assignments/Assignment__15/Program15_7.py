#######################################################################################
#   Function name   :   StringLen
#   Description     :   Returns list of strings whose length are greater than 5
#   Input           :   List
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   19/01/26
#######################################################################################

StringLen = lambda string : string if len(string) > 5 else False

def main():
    Ret = list()
    Data = ["Hello","There","Mrunmai","Name","Sanika","Shraddha","Ganesh"]
    
    Ret = list(filter(StringLen,Data))

    print("Strings whose length is greater than 5 are:",Ret)

if __name__ == "__main__":
    main()