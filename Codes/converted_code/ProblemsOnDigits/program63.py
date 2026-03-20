

def main():
    iNo = 723614
    iDigit = 0
    Border = "-"*50

    print(Border)
    print("Original value of iNo is : ",iNo)
    print(Border)

    iDigit = iNo % 10
    print("iDigit is : ",iDigit)
    iNo = iNo//10
    print("iNo is : ",iNo)

    print(Border)
    iDigit = iNo % 10
    print("iDigit is : ",iDigit)
    iNo = iNo//10
    print("iNo is : ",iNo)

    print(Border)
    iDigit = iNo % 10
    print("iDigit is : ",iDigit)
    iNo = iNo//10
    print("iNo is : ",iNo)

    print(Border)
    iDigit = iNo % 10
    print("iDigit is : ",iDigit)
    iNo = iNo//10
    print("iNo is : ",iNo)
    print(Border)
    
if __name__ == "__main__":
    main()