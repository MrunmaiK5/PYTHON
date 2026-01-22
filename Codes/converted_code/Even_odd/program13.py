def CheckEvenOdd(No):
    Rem = 0 
    Rem = No % 2

    if Rem ==  0:
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter a number:")
    Value = float(input())

    Ret = CheckEvenOdd(Value)

    print("Resutl :",Ret)


if __name__ == "__main__":
    main() 
