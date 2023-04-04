print("1"," for +,", "2", "for -")
user= int(input())

a= int (input ("a="))
b= int (input ("b="))



if user== 1:
    op1=a+b
    print(f'a+b={op1}')
elif user ==2:
    op2=a-b
    print(f'a-b={op2}')
else:
    user != 1 or 2
    print("WRONG!")


