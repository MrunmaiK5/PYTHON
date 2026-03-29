class ArrayX:

    def Display(Brr):
        for i in range(len(Brr)):
            print(Brr[i])

def main():
    Arr = []

    print("Number of elements is :",len(Arr))

    Arr.append(10)
    Arr.append(20)
    Arr.append(30)
    Arr.append(40)

    aobj = ArrayX()

    aobj.Display(Arr)

    
if __name__ == "__main__":
    main()