import os 

########################################################################################################
#   Function name   :   CountWords
#   Description     :   Counts number of words in file
#   Input           :   String
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   04/02/26
########################################################################################################

def CountWords(fName):
    Count = 1
    Ret = os.path.exists(fName)

    if Ret == True:
        fobj = open(fName,"r")
        Data = fobj.read()

        for words in Data:
            if words == '\n' or words == ' ':
                Count += 1
        
        return Count
    
    else:
        print("No such file exists")


def main():
    FileName = input("Enter file name : ")
    Result = CountWords(FileName)
    print("Count of words is :",Result)

if __name__ == "__main__":
    main()