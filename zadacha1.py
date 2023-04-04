x = int (0)

while True:
    hh = int (input ("Enter your number:"))
    print (hh)
    if int(hh) < 0:
        break
    if hh > 0:
        x = x + hh
        print (x)
print (x)