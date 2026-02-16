import time
import datetime

def main():
    print(time.time())      #epoch time - 1 jan 1970 12 am
    print(time.ctime())     #
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()