def Add(a,b):
    sum = 0
    sum= a + b
    return sum

def main():
    i = 0
    j = 0
    ans = 0

    print("Enter first number:")
    i = int(input())

    print("Enter second number:")
    j = int(input())

    ans = Add(i,j)
    print("Addition is:",ans)


if __name__ == "__main__":
    main() 
