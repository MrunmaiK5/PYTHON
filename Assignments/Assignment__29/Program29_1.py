import os 
########################################################################################################
#   Function name   :   ExistsX
#   Description     :   Checks whether given file exists in user current directory
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   03/02/26
########################################################################################################

def ExistsX(fName):

    Ret = os.path.exists(fName)

    if (Ret == True):
        print("File exists")
    else:
        print("There is no such file")


def main():
    FileName = input("Enter file name : ")
    ExistsX(FileName)

if __name__ == "__main__":
    main()