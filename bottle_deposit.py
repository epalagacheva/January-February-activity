#Half liter bottles have $0.1 deposit and the one liter bottles have $0.25 deposit. 
#Calculate the sum which you will make when returning the bottles. 
#You must print two digits after the decimal point.
small_b=int(input())
large_b=int(input())

sum_small=small_b*0.1
sum_large=large_b*0.25

sum_total=round(sum_small+sum_large, 2)

print("%.2f" % sum_total)