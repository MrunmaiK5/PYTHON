def CountFactorsNonFactors(iNo):
    iCount1 = 0
    iCount2 = 0

    if iNo < 0:
        iNo = -iNo
        
    for i in range(1,iNo):
        if ( (iNo%i) != 0 ):
            iCount1 = iCount1 + 1
        else:
            iCount2 = iCount2 + 1
    
    print("Number of factors : ",iCount2)
    print("Number of non factors : ",iCount1)
    

def main():
    iValue = 0

    iValue = int(input("Enter the no : "))

    CountFactorsNonFactors(iValue)
    
if __name__ == "__main__":
    main()