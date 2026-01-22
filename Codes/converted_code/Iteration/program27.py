def Display(freq):
    if freq < 0:
        print("Invalid input")
        
    for i in range(freq):
        print("Jay Ganesh...")
    
def main():
    Frequency = 0
    print("Enter the frequency:")
    Frequency = int(input())
    Display(Frequency)

if __name__ == "__main__":
    main() 
