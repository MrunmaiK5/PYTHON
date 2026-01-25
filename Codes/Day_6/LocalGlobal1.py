no = 11             # Gloabl

def Fun():
    no = 21         # Local
    print("Value of no from Fun() is: ",no) #21

print("Value of no is: ",no)        #11
Fun()