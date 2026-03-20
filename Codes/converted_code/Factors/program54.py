def CheckPrime(iNo):
    iCount = 0

    if iNo < 0:
        iNo = -iNo
        
    for i in range(2,(iNo//2)+1):
        if ( (iNo%i) == 0 ):
            iCount = iCount + 1
    
    if iCount == 0:
        return True
    else:
        return False

def main():
    iValue = 0

    iValue = int(input("Enter the no : "))

    Ret = CheckPrime(iValue)

    if (Ret == True):
        print(iValue," is prime number")
    else:
        print(iValue," is not a prime number")
    
if __name__ == "__main__":
    main()