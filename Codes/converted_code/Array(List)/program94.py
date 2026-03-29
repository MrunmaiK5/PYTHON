class ArrayX:

    def Display(Brr):
        for i in range(len(Brr)):
            print(Brr[i])


def main():
    Arr = [10,20,30,40]

    aobj = ArrayX()

    aobj.Display(Arr)

    
if __name__ == "__main__":
    main()