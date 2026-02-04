import os 
########################################################################################################
#   Function name   :   ReadX
#   Description     :   Displays contents of user given file on console
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   03/02/26
########################################################################################################

def ReadX(fName):

    Ret = os.path.exists(fName)

    if (Ret == True):
        fobj = open(fName,"r")
        print(fobj.read())
    else:
        print("There is no such file")


def main():
    FileName = input("Enter file name : ")
    ReadX(FileName)

if __name__ == "__main__":
    main()