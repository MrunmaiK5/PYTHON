class ArrayX:

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

    
if __name__ == "__main__":
    main()