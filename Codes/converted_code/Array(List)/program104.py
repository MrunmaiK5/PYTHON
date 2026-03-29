class ArrayX:
    Arr = []
    iSize = 0

    def __init__(self,No):
        self.iSize = No 
        self.Arr = [0] * self.iSize

    def Accept(self):
        print("Enter elements : ")
        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def Displau(self):
        print("Elements are : ")
        for i in range(self.iSize):
            print(self.Arr[i])

def main():
    aobj = ArrayX()
    
if __name__ == "__main__":
    main()