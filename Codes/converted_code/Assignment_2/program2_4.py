
###########################################################################################################
#
#  Function name   : Display
#  Description     : Accepts 2 numbers and diplays the first number with frequency given as second number
#  Input           : Integer
#  Output          : Nothing
#  Author          : Mrunmai Jitendra Khadpe
#  Date            : 31/03/2026
#
###########################################################################################################

def Display(iNo, Freq):
    for i in range(Freq):
        print(iNo)

def main():
    
    No = int(input("Enter a number : "))
    Freq = int(input("Enter frequency : "))

    Display(No, Freq)

if __name__ == "__main__":
    main()