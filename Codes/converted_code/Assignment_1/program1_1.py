
###########################################################################
#
#  Function name   : Divide
#  Description     : Division of two numbers
#  Input           : Integer, Integer
#  Output          : Integer
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################

def Divide(iNo1, iNo2):
    iAns = 0

    if iNo1 == 0:
        return -1
    
    iAns = iNo1 / iNo2 

    return iAns

def main():
    iValue1 = 15
    iValue2 = 5
    iRet = 0 

    iRet = Divide(iValue1, iValue2)
    print("Division is : ",iRet)

if __name__ == "__main__":
    main()