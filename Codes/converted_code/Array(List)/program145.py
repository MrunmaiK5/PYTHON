def Maximum(Arr, No, Size):
    iMax = Arr[0]
    for i in range(Size):
        if iMax < Arr[i]:
            iMax = Arr[i]
    
    return iMax

def main():
    Size = int(input("Enter size of an array : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Ret = Maximum(Arr, Size)
    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()