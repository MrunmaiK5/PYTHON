
###########################################################################
#
#  Function name   : Display
#  Description     : Display * as per user input
#  Input           : Integer
#  Output          : Nothing
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################

def Display(iNo):
    while iNo > 0:
        print("*")
        iNo = iNo - 1

def main():
    
    No = int(input("Enter a number : "))

    Display(No)

if __name__ == "__main__":
    main()