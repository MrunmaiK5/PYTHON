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

    def Average(self):
        iSum = 0

        for i in self.Arr:
            iSum = iSum + i
        
        return (iSum / len(self.Arr))

def main():
    fRet = 0.0

    aobj1 = ArrayX(5)
    aobj1.Accept()
    fRet = aobj1.Average()
    aobj1.Display()

    print("Average : ",fRet)
    
if __name__ == "__main__":
    main()