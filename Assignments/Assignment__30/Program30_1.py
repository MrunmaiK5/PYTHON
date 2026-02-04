import os 

########################################################################################################
#   Function name   :   CountLines
#   Description     :   Counts number of lines in file
#   Input           :   String
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   04/02/26
########################################################################################################

def CountLines(fName):
    Count = 1

    Ret = os.path.exists(fName)

    if Ret == True:
        fobj = open(fName,"r")
        Data = fobj.read()

        for lines in Data:
            if lines == '\n':
                Count += 1
        
        return Count
    
    else:
        print("No such file exists")


def main():
    FileName = input("Enter file name : ")
    Result = CountLines(FileName)
    print("Count of lines is :",Result)

if __name__ == "__main__":
    main()