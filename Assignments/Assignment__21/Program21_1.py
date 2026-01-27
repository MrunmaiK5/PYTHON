import threading

#######################################################################################
#   Function name   :   Prime
#   Description     :   Displays prime numbers from given list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Prime(Arr):
    print("Prime numbers :")
    
    for num in Arr:
        for i in range(2,num):
            if i < 2 and i >= 0:
                print(num," is neither prime nor composite", end="\t")

            if num%i == 0:
                break
    
        if i >= num-1:
            print(num, end="\t")

    print()


#######################################################################################
#   Function name   :   NonPrime
#   Description     :   Displays non prime numbers from given list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def NonPrime(Arr):
    print("Non-Prime numbers :")
    
    for num in Arr:
        for i in range(2,num):
            if i < 2 and i >= 0:
                print(num," is neither prime nor composite", end="\t")

            if num%i == 0:
                print(num, end="\t")
                break
    
            
    print()

def main(): 
    Brr = [34,31,2,13,73,7,23]

    t1 = threading.Thread(target=Prime, args=(Brr,))
    t2 = threading.Thread(target=NonPrime, args=(Brr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()