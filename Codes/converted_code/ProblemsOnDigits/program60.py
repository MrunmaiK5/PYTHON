

def main():
    iNo = 7236
    iDigit = 0

    iDigit = iNo % 10
    print(iDigit)
    iNo = iNo//10

    iDigit = iNo % 10
    print(iDigit)
    iNo = iNo//10

    iDigit = iNo % 10
    print(iDigit)
    iNo = iNo//10

    iDigit = iNo % 10
    print(iDigit)
    iNo = iNo//10
    
if __name__ == "__main__":
    main()