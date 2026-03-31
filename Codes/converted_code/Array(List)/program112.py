def Display(Arr):
    iCnt = 0
    for iCnt in range(4):
        print(Arr[iCnt])

def main():
    Arr = [10,20,30,40]

    for i in range(4):
        print(Arr[i])

    Display(Arr)
    
if __name__ == "__main__":
    main()