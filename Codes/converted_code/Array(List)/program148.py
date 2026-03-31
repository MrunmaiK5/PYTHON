def Update(Arr, Size):
    for i in range(Size):
        Arr[i] = Arr[i] + 1
    

def main():
    Size = int(input("Enter size of an array : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    Update(Arr, Size)

if __name__ == "__main__":
    main()