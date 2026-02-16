import os

def main():
    FileName = input("Enter the name of file :")

    Ret = os.path.isabs(FileName)

    if (Ret == True):
        print("File path exists")
    else:
        print("There is no such path")

if __name__ == "__main__":
    main()
