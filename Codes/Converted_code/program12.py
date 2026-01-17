def CheckEvenOdd(No):
    Rem = 0 
    Rem = No % 2

    if Rem ==  0:
        print("It is an even number\n")
    else:
        print("It is an odd number\n")

def main():
    Value = 0

    print("Enter a number:")
    Value = float(input())

    CheckEvenOdd(Value)


if __name__ == "__main__":
    main() 
