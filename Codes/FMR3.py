from functools import reduce

def CheckEven(No):
    return (No%2 == 0)

def Increment(No):
    return (No+1)

def Add(A, B):
    return (A + B)

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is: ", Data)

    # filter should give such a function which accepts only one input and give boolean
    FData = list(filter(CheckEven, Data))   # if not converted to list it gives id of location where the filtered data is stored
    print("Data after filter is:",FData)

    MData = list(map(Increment, FData))
    print("Data after mapping is:",MData)

    RData = reduce(Add, MData)
    print("Data after reduce is:",RData)


if __name__ == "__main__":
    main() 