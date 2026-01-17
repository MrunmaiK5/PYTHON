def CheckEvenOdd(No):
    if (No%2) ==  0:
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter a number:")
    Value = float(input())

    Ret = CheckEvenOdd(Value)

    if Ret == True:
        print(Value, " is an even number")
    else:
        print(Value, " is an odd number")


if __name__ == "__main__":
    main() 
