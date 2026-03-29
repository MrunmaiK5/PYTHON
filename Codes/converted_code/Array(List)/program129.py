def CountEven(Arr, Size):
    iEven = 0
    for i in range(Size):
        iEven = iEven + Arr[i]

    return iEven

def main():
    Size = int(input("Enter size of an arrya : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Ret = CountEven(Arr, Size)
    print("Count of even elements : ",Ret)
    
if __name__ == "__main__":
    main()