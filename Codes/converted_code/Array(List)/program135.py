def FrequencyCalculate(Arr, No, Size):
    iCount = 0
    for i in range(Size):
        if No == Arr[i]:
            iCount = iCount + 1

    return iCount

def main():
    Size = int(input("Enter size of an array : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    No = int(input("Enter element to search : "))
    
    Ret = FrequencyCalculate(Arr, No, Size)
    print("Frequency of number is : ",Ret)
    
if __name__ == "__main__":
    main()