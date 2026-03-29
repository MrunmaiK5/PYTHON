def Summation(Arr, Size):
    iSum = 0
    for i in range(Size):
        iSum = iSum + Arr[i]

    return iSum

def main():
    Size = int(input("Enter size of an arrya : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Ret = Summation(Arr, Size)
    print("Summation of elements : ",Ret)
    
if __name__ == "__main__":
    main()