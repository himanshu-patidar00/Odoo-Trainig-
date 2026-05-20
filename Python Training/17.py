balance = 0 
while(True):
    want = input("D/w like D 500 W 400  or exit : ") 
    if(want.lower()=="exit"):
        break 
    try:
        act,amount = want.split() 
        amount = int(amount) 
        
        if(act.upper()=="D"):
            balance += amount 
        elif(act.upper()=="W"):
            if(balance>=amount):
                balance -= amount
            else:
                print("INSufficient balance") 
        else:
            print("Invalid transaction  type ")
    except ValueError:
        print("Invalid Inputs")
    
print("Final Balance : ",balance) 