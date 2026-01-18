#######################################################################################
#   Function name   :   CountDigits
#   Description     :   Returns number of digits from given number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def CountDigits(a):
    Count = 0
    while a > 0:
        a = int(a/10)
        Count = Count + 1

    return Count

def main():
    Ret = CountDigits(7521)
    
    print("No. of digits are :",Ret)

if __name__ == "__main__":
    main()