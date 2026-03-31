
###########################################################################
#
#  Function name   : Display
#  Description     : Display Hello if number is less than 10 else print Demo
#  Input           : Integer
#  Output          : Nothing
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################

def Display(iNo):
    if iNo < 10:
        print("Hello")
    else:
        print("Demo")

def main():
    
    No = int(input("Enter a number : "))

    Display(No)

if __name__ == "__main__":
    main()