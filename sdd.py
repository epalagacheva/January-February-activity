print ("Hello World1")

message = "hello Bozho2"
print (message)

message = 'hellooo'
name = "Bozho"
message = f'hellooo {name}'
print(message)

greeting = 'hello ' 'Sunshine '
print(greeting)

greeting = greeting + name + "!"
print(greeting)

str = "Bozho"
new_str = "Emi"
greeting = 'hello ' 'Sunshine '
print ((greeting[0:15]) + (new_str) + '!') 

#hi = greeting + new_str
#print(hi)

def main():
    i=1
    max = 10
    while (i < max):
        print(i)
        i=i+2



main()

greeting = 'good morning, Ala Bala!'
autor = 'thank you, so very much..'
autor = autor + greeting
#greeting = greeting + autor
print(autor)

str = "Pitonq Harabiq"
print(str[0])

#price = input('Enter a price:')
#tax = input('Enter a tax rate %:')
#net_price = int (price) * int(tax) / 100
#print(f'The net price is {net_price}')

a=10
b=2
if a<b:
    print ('a e po-malko ot b')
else:
    print ('b e po-malko ot a')

age = input ('enter your age:')
if int(age) >= 18:
    print ('Moe da glasuvash')
else:
    print ('ne moe')

age = input('Enter your age:')

# convert the string to int
your_age = int(age)

# determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

# show the ticket price
print(f"You'll pay ${ticket_price} for the ticket")
