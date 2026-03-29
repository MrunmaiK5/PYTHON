def Average(Arr, Size):
    iSum = 0
    for i in range(Size):
        iSum = iSum + Arr[i]

    return (iSum / Size)

def main():
    Size = int(input("Enter size of an arrya : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Ret = Average(Arr, Size)
    print("Average is : ",Ret)
    
if __name__ == "__main__":
    main()