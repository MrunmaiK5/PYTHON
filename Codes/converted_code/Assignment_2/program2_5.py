
###########################################################################################################
#
#  Function name   : ChkEven
#  Description     : Check if given number is even or odd
#  Input           : Integer
#  Output          : Boolean
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################################################

def ChkEven(iNo):
    if iNo < 0:
        iNo = -iNo

    if (iNo % 2 == 0):
        return True
    else:
        return False

def main():
    
    No = int(input("Enter a number : "))

    Ret = ChkEven(No)

    if Ret == True:
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()