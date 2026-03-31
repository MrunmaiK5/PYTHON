import gc
def main():
    Size = int(input("Enter size of an arrya : "))
    Arr = [0] * Size

    print("Enter elements : ")

    for i in range(Size):
        Arr[i] = int(input())
    
    del Arr 
    gc.collect()
    
if __name__ == "__main__":
    main()