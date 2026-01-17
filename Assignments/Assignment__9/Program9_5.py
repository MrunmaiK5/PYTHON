def Divisible(a):
    if (a%3 == 0) and (a%5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible")


def main():
    Divisible(15)

if __name__ == "__main__":
    main()