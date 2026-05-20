# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play","Love"] and the object is in ["Hockey","Football"].



sub =["I","You"] 
verb = ["play","love"]
obj = ["hockey","football"] 

for s in sub:
    for v in verb:
        for o in obj:
            print(f"{s} {v} {o}")  
 
 