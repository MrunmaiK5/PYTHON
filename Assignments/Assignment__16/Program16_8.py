#######################################################################################
#   Function name   :   Display
#   Description     :   Displays number of * given by user in a row 
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def Display(No):
    for i in range(No):
        print("*", end="\t")

def main():
    No = 0
    No = int(input("Enter a number :"))
    Display(No)

if __name__ == "__main__":
    main()