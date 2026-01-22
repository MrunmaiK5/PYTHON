def Display(Value):
    for i in range(2, Value+1, 2):
        print(i)

def main():
    Value = 0
    print("Enter frequency: ")
    Value = int(input())
    Display(Value)

if __name__ == "__main__":
    main() 
