import os 
import sys

########################################################################################################
#   Function name   :   CopyX
#   Description     :   Copies content from one file to new file Demo.txt
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   03/02/26
########################################################################################################

def CopyX(fName):

    Ret = os.path.exists(fName)

    if (Ret == True):
        fobj = open(fName,"r")
        newobj = open("Demo.txt","a")

        Data = fobj.read()
        Result = newobj.write(Data)
         
        if Result > 0:
            print("Sucessfully copied the contents")

    else:
        print("There is no such file")


def main():
    
    if len(sys.argv) != 2 :
        print("Invalid parameters")
        print("Please enter valid parameter")
        return

    CopyX(sys.argv[1])

if __name__ == "__main__":
    main()