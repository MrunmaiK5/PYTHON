def CountFactors(iNo):
    iCount = 0
    if iNo < 0:
        iNo = -iNo
        
    for i in range(1,(iNo//2)+1):
        if ( (iNo%i) == 0 ):
            iCount = iCount + 1

    return iCount

def main():
    iValue = 0

    iValue = int(input("Enter the no : "))

    Ret = CountFactors(iValue)
    print("Number of factors are : ",Ret)

if __name__ == "__main__":
    main()