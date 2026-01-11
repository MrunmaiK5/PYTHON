no = 11             # Gloabl

def Fun():
    global no   #refers to outside variable
    print("Value of no from Fun() is: ",no) #11
    no = no+1   #12
    print("Value of no from Fun() is: ",no) #12

print("Value of no is: ",no)   #11     
Fun()
print("Value of no is: ",no)   #12