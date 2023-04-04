#vuvejdash chisla dokato ne vuvedesh otricatelno chislo i sled tova programata gi izpisva
hh = int(input ("Enter your number"))
print (hh)
numbers = []
while True:
    numbers.append(hh)
    hh= int (input ("Enter your number:"))
    if int(hh) < 0:
        break

print (hh)

print (numbers)
gg = int (sum(numbers))
print (gg)
