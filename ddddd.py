for x in range (0,2):
    print ('hello %s' % x)

wizzard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing']
for i in wizzard_list:
    print (i)

a= int(input("a="))
print (a)
b= int(input("b="))
print (b)
c= int (input("c="))

list= [a,b,c]
newlist= sorted (list)
print (newlist)

newlist_reverse = sorted(list, reverse=True)
print(newlist_reverse)

word="google.com"
counter_dict = dict()

for char in word:
    if char in counter_dict.keys():
        counter_dict[char] += 1
    else:
        counter_dict[char] = 1

print(counter_dict)