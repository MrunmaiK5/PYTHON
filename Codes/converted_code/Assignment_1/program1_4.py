
###########################################################################
#
#  Function name   : Check
#  Description     : Checks whether number is divisible by 5
#  Input           : Integer
#  Output          : Boolean
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################

def Check(iNo):
    if iNo % 5 == 0:
        return True
    else:
        return False

def main():

    No = int(input("Enter a number : "))

    Ret = Check(No)

    if Ret == True:
        print("No is divisible")
    else:
        print("No is not divisible")

if __name__ == "__main__":
    main()