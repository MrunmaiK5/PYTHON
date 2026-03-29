def CountOdd(Arr, Size):
    iOdd = 0
    for i in range(Size):
        iOdd = iOdd + Arr[i]

    return iOdd

def main():
    Size = int(input("Enter size of an arrya : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Ret = CountOdd(Arr, Size)
    print("Count of odd elements : ",Ret)
    
if __name__ == "__main__":
    main()