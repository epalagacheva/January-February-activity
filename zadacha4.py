#sravnenie na 3 chisla
a=int(input("a=")) #10
b=int(input("b=")) #6
c=int(input("c=")) #11

if a>b:
    if a>c:
        max = a
        if b>c:
            min=c
            mid=b
        else:
            #c>b
            min=b
            mid=c
    else:
        #c>a
        max=c
else:
    #b>a
    if b>c:
        max=b
        if c>a:
            #c<b
            mid=c
            min=a
        else:
            #a>c
            mid=a
            min=c
    else:
        max=c
        mid=b
        min=a

print (max,mid, min)
print (min, mid,max)