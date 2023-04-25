#converter
import math
m=int(input())
km=int(m*1.6)
galon=4.54

result=math.floor(((100*galon)/km))

print(f'{result} litres per 100km')