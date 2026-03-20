def SumDigits(iNo):
    iSum = 0
    iDigit = 0
    Border = "-"*50

    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + 1
        iNo = iNo//10

    return iSum

def main():
    iNo = 0
    
    iNo = int(input("Enter a number : "))

    Ret = SumDigits(iNo)
    print("Sum of digits :", Ret)
    
if __name__ == "__main__":
    main()