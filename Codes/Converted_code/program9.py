def AdditionTwoNumbers(No1, No2):
    sum = 0
    if No1 < 0:
        No1 = -No1

    if No2 < 0:
        No2 = -No2
        
    sum= No1 + No2
    return sum

def main():
    Value1 = 0.0
    Value2 = 0.0
    Ret = 0.0

    print("Enter first number:")
    Value1 = float(input())

    print("Enter second number:")
    Value2 = float(input())

    Ret = AdditionTwoNumbers(Value1,Value2)
    print("Addition is:",Ret)


if __name__ == "__main__":
    main() 
