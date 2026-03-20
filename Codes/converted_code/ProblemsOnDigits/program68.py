def CountDigits(iNo):
    iDigit = 0
    iCount = 0
    Border = "-"*50

    print(Border)
    print("Original value of iNo is : ",iNo)

    while(iNo != 0):
        print(Border)
        iDigit = iNo % 10
        iCount = iCount + 1
        iNo = iNo//10

    return iCount

def main():
    iNo = 0
    
    iNo = int(input("Enter a number : "))

    Ret = CountDigits(iNo)
    print("Count of digits :", Ret)
    
if __name__ == "__main__":
    main()