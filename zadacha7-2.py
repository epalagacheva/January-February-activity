#obrushtane na vuvedena kalendarna data ot user 
v=input("Your date is:")
v=v.lower()
v=v.split('.')
#print (len(v))

#print(len(v[0]))

# if len(v[2]) == 1:
#     print (v[3][:2])
# if len(v[2]) == 3:
#     print (v[3][:4])


# if len(v[0]) == 0:
#     print (v[1][:1])
# if len(v[0]) == 1:
#     print (v[1][:2])


# if len(v[1]) == 0:
#     print (v[1][:1])
# if len(v[1]) == 1:
#     print (v[1][:2])

print (v[2] + '.' + v[0] +'.'+  v[1])