from MarvellousFMR import filterX, mapX, reduceX

CheckEven = lambda No: (No%2 == 0)
Increment = lambda No: (No+1)
Add = lambda A, B: (A + B)

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is: ", Data)

    # filter should give such a function which accepts only one input and give boolean
    FData = list(filterX(CheckEven, Data))   # if not converted to list it gives id of location where the filtered data is stored
    print("Data after filter is:",FData)

    MData = list(mapX(Increment, FData))
    print("Data after mapping is:",MData)

    RData = reduceX(Add, MData)
    print("Data after reduce is:",RData)


if __name__ == "__main__":
    main() 