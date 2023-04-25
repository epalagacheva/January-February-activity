#print the amount in your deposit for each of the 3 years
#number with two numbers after the decimal point 5%
money=int(input())

first_year=float(money + ((5/100)*money))
print ("%.2f" % first_year)

second_year=float(first_year + ((5/100)*first_year))
print ("%.2f" % second_year)

thirth_year=float(second_year + ((5/100)*second_year))
print ("%.2f" % thirth_year)
