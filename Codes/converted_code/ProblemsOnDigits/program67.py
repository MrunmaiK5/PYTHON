def DisplayDigits(iNo):
    iDigit = 0
    Border = "-"*50
    print(Border)
    print("Original value of iNo is : ",iNo)

    while(iNo != 0):
        print(Border)
        iDigit = iNo % 10
        print("iDigit is : ",iDigit)
        iNo = iNo//10
        print("iNo is : ",iNo)

def main():
    iNo = 0
    
    iNo = int(input("Enter a number : "))

    DisplayDigits(iNo)
    
if __name__ == "__main__":
    main()