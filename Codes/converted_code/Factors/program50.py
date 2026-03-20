def DisplayFactors(iNo):
    
    if iNo < 0:
        iNo = -iNo
        
    for i in range(1,(iNo//2)+1):
        if ( (iNo%i) == 0 ):
            print(i)

def main():
    iValue = 0

    iValue = int(input("Enter the no : "))

    DisplayFactors(iValue)

if __name__ == "__main__":
    main()