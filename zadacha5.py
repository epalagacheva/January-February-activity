# vuvejdane na 5 chisla i programata da nameri naj golqmoto
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
e=int(input("e="))


if a>b:
    max=a
else:
    b=max
    if b>c:
        if b>d:
            if b>e:
                max=b
            else:
                max=e
        else:
            max=d
    else:
        max=c

print (max)