def AdditionTwoNumbers(No1, No2):
    sum = 0
    sum= No1 + No2
    return sum

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number:")
    Value1 = int(input())

    print("Enter second number:")
    Value2 = int(input())

    Ret = AdditionTwoNumbers(Value1,Value2)
    print("Addition is:",Ret)


if __name__ == "__main__":
    main() 
