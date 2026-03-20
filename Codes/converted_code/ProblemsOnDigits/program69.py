def CountDigits(iNo):
    iCount = 0
    Border = "-"*50

    while(iNo != 0):
        print(Border)
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