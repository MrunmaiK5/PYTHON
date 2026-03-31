def ReverseDisplay(Arr, Size):
    for i in range(Size-1,-1, -1):
        print(Arr[i])
    

def main():
    Size = int(input("Enter size of an array : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    ReverseDisplay(Arr, Size)

if __name__ == "__main__":
    main()