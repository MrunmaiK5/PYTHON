import os 

########################################################################################################
#   Function name   :   CopyNew
#   Description     :   Copies content from existing file into new file
#   Input           :   String, String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   04/02/26
########################################################################################################

def CopyNew(src, dest):
    Count = 1
    Ret = os.path.exists(src)

    if Ret == True:
        sobj = open(src,"r")

        dobj = open(dest,"w")

        Data = sobj.read(1024)

        while len(Data) > 0:
            dobj.write(Data)
            Data = sobj.read(1024)   

        print("Successfully copied contents")   
    
    else:
        print("No source file exists")


def main():
    Source = input("Enter source file name : ")
    Destination = input("Enter destination file name : ")
    
    CopyNew(Source, Destination)

if __name__ == "__main__":
    main()