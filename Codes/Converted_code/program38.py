def Display(Value):
    for i in range(Value, 0, -1):
        print(i)

def main():
    Value = 0
    print("Enter frequency: ")
    Value = int(input())
    Display(Value)

if __name__ == "__main__":
    main() 
