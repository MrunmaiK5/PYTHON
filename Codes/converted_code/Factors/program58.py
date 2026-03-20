def CheckPrime(iNo):
    bFlag = False

    if iNo < 0:
        iNo = -iNo
        
    bFalg = True
    for i in range(2, int((iNo/2)+1)):
        if ( (iNo%i) == 0 ):
            bFlag=False
            break
    
    return bFlag

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