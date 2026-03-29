from sys import getsizeof
def main():
    Arr = [10,20,30,40]

    print("Arr : ",Arr)
    print("Address of array : ",id(Arr))
    print("Address of first element of array : ",id(Arr[0]))
    print("Size of array : ",getsizeof(Arr))
    
if __name__ == "__main__":
    main()