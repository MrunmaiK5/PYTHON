def LinearSearch(Arr, No, Size):

    for i in range(Size):
        if No == Arr[i]:
            break
    
    return (i == Size)

def main():
    Size = int(input("Enter size of an array : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    No = int(input("Enter element to search : "))
    
    Ret = LinearSearch(Arr, No, Size)
    if Ret == True:
        print(" Element is present ")
    else:
        print(" Element is not present ")
if __name__ == "__main__":
    main()