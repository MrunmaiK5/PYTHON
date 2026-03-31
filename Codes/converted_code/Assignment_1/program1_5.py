
###########################################################################
#
#  Function name   : Accept
#  Description     : Display * as per user input
#  Input           : Integer
#  Output          : Nothing
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################

def Accept(iNo):
    for i in range(iNo):
        print("*", end = "")

def main():
    
    No = int(input("Enter a number : "))

    Accept(No)

if __name__ == "__main__":
    main()