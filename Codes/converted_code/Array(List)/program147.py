def Minimum(Arr, No, Size):
    iMin = Arr[0]
    for i in range(Size):
        if iMin > Arr[i]:
            iMin = Arr[i]
    
    return iMin

def main():
    Size = int(input("Enter size of an array : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Ret = Minimum(Arr, Size)
    print("Minimum is : ",Ret)

if __name__ == "__main__":
    main()