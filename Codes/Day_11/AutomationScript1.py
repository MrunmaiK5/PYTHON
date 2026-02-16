import sys

def main():
    border = "-"*40
    print(border)
    print("--------- Marvellous Automation --------")
    print(border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")): 
            print("this application is used to perform ____")
            print("this is automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")): 
            print("Use the keyword script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : _______________")
            print("Argument2 : _______________")

        else:
            print("Use the given flags as: ")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as: ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(border)
    print("---- Thank you for using our script ----")
    print("-------- Marvellous Infosystems --------")
    print(border)

if __name__ == "__main__":
    main()