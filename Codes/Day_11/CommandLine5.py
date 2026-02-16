# CommandLine3.py 11 10

import sys

def main():
    if(len(sys.argv) < 3 or len(sys.argv) > 3):
        print("Invalid number of agrguments")
    else:
        print("Addition:",int(sys.argv[1])+int(sys.argv[2]))

if __name__ == "__main__":
    main() 