class ArrayX:

    def CountEven(Brr):
        iCount = 0
        for i in range(len(Brr)):
            if Brr[i] % 2 == 0:
                iCount = iCount + 1

        return iCount

    def Display(Brr):
        for i in range(len(Brr)):
            print(Brr[i])

def main():
    Arr = []
    Size = 0 

    Size = int(input("Enter number of elements : "))

    print("Enter elements : ")

    for i in range(Size):
        Arr.append(int(input()))

    aobj = ArrayX()

    aobj.Display(Arr)
    Ret = aobj.CountEven(Arr)
    print("Count of even number is :",Ret)

    
if __name__ == "__main__":
    main()