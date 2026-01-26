import threading

Sum = 0
Product = 1

#######################################################################################
#   Function name   :   SumOfElements
#   Description     :   Calculates sum of elements of list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def SumOfElements(Arr):
    global Sum

    for num in Arr:
        Sum = Sum + num


#######################################################################################
#   Function name   :   ProdcOfElements
#   Description     :   Calculates producat of elements of the list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def ProdcOfElements(Arr):
    global Product

    for num in Arr:
        Product = Product * num

def main(): 

    Brr = list()

    Size = int(input("Enter size of list :"))

    print("Enter elements :")
    for i in range(Size):
        Brr.append(int(input()))

    t1 = threading.Thread(target=SumOfElements, args=(Brr,))
    t1.start()
    t1.join()

    print("Sum of elements :",Sum)

    t2 = threading.Thread(target=ProdcOfElements, args=(Brr,))
    t2.start()
    t2.join()

    print("Product of elements :",Product)

if __name__ == "__main__":
    main()