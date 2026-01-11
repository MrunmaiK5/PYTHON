def main():
    size = 0

    print("Enter the number of elements: ")
    size = int(input())

    Data = list()

    print("Enter the elements: ")
    for i in range(size):
        value = int(input())
        Data.append(value)

    sum = 0

    for i in range(size):
        sum = sum + Data[i]
    
    print("Summation:",sum)

if __name__ == "__main__":
    main()