#######################################################################################
#   Function name   :   ChkGreater
#   Description     :   Displays the greater number from given two numbers
#   Input           :   Integer, Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def ChkGreater(a, b):
    if a > b:
        print(a)
    else:
        print(b)

def main():
    ChkGreater(10,20)

if __name__ == "__main__":
    main()