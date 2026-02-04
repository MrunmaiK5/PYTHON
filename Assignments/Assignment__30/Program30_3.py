import os 

########################################################################################################
#   Function name   :   DisplayLines
#   Description     :   Displays content of file line by line
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   04/02/26
########################################################################################################

def DisplayLines(fName):
    Count = 1
    Ret = os.path.exists(fName)

    if Ret == True:
        fobj = open(fName,"r")

        for line in fobj:
            print(line, end='\n')      
    
    else:
        print("No such file exists")


def main():
    FileName = input("Enter file name : ")
    
    DisplayLines(FileName)

if __name__ == "__main__":
    main()