def DisplayFactors(iNo):
    if ((iNo%1) == 0):
        print("1")
    if ((iNo%2) == 0):
        print("2")
    if ((iNo%3) == 0):
        print("3")
    if ((iNo%4) == 0):
        print("4")
    if ((iNo%5) == 0):
        print("5")

def main():
    iValue = 0

    iValue = int(input("Enter the no : "))

    DisplayFactors(iValue)

if __name__ == "__main__":
    main()