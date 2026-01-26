import threading

#######################################################################################
#   Function name   :   Max
#   Description     :   Displays largest number from the list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Max(Arr):
    max = Arr[0]

    for num in Arr:
        if num > max:
            max = num
    
    print("Maximum number is :",max)

    print()


#######################################################################################
#   Function name   :   Min
#   Description     :   Displays smallest element from the list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Min(Arr):
    min = Arr[0]

    for num in Arr:
        if num < min:
            min = num
    
    print("Minimum number is :",min)

    print()

def main(): 

    Brr = list()

    Size = int(input("Enter size of list :"))

    print("Enter elements :")
    for i in range(Size):
        Brr.append(int(input()))

    t1 = threading.Thread(target=Max, args=(Brr,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Min, args=(Brr,))
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()