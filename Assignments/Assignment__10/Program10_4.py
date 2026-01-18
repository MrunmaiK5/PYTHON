#######################################################################################
#   Function name   :   EvenNum
#   Description     :   Displays even n natural numbers
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def EvenNum(a):
    for i in range(1,a+1):
        if i%2 == 0:
            print(i)

def main():
    EvenNum(15)

if __name__ == "__main__":
    main()