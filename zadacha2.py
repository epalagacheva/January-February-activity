#a/b c-kolko puti da se napravqt deleniq, b!=0
d=int (input ("kolko deleniq da napravq?:"))

f=1
for f in range (d):
    a=int (input("a="))
    b=int (input("b="))
    
    if b==0:
        print ("Imposible")
    else:
        c=a/b
    
    print (f"(c= {c}")

print (c)


    
