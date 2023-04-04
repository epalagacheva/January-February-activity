

#def maximum(a,b,c):
    #find max
 #   a=int
  #  b=int
    #c=int
   # if a > b :
   #     if a > c :
    #        return a
     #   return c
    #if b > c :
     #   return b
    #return c    
#maximum (20,3,45)}

def max_of_2 (x,y):
    if x>y:
        return x
    return y

def max_of_3 (z,x,y):
    return max_of_2(z,max_of_2(x,y))
print(max_of_3(78,2,100))


def sumi (numbers):
    vsichko=0
    for x in numbers:
        vsichko += x
    return vsichko    
print (sumi ((2,10,50)))


#def reve(ctr):
    #reversed=''.join(reversed(ctr))
    #print(reversed)
#reve("1234abcd")


def greet(name, message='Hi'):
    return f"{message} {name}"

greeting = greet('John', 'Hello')
print(greeting)

def get_net_price(price, discount):
    return price * (1-discount)
    
net_price = get_net_price(100, 0.1)
print(net_price)