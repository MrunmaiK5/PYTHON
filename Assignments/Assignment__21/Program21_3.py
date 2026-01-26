import threading

SharedCounter = 0
lock = threading.Lock()

#######################################################################################
#   Function name   :   Thread1, Thread2
#   Description     :   Updates the shared counter.
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Thread1():
    global SharedCounter

    for i in range(500):
        lock.acquire()
        SharedCounter += 3
        lock.release()

def Thread2():
    global SharedCounter

    for i in range(500):
        lock.acquire()
        SharedCounter -=1
        lock.release()

def main(): 
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Counter :",SharedCounter)


if __name__ == "__main__":
    main()