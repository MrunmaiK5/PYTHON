no = 11             # Gloabl

def Fun():
    no=21
    print("Value of no from Fun() is: ",no) 
    no = no+1   #considers no as local initialization so gives error (if not initialized any variable before i.e no = 21)
    print("Value of no from Fun() is: ",no) 

print("Value of no is: ",no)        
Fun()
print("Value of no is: ",no)        