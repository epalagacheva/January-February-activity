#1 hour of free calls and 20 text messages for 12.00 levas 
#additional minute costs 0.10 levas +20% tax
#additional message costs 0.06 levas +20% tax
total_text=int(input())
total_minutes=int(input())

import math
plan_minutes=60
plan_text=20
plan_price=12

add_text=total_text-plan_text
add_minutes=total_minutes-plan_minutes

if add_text > 0:
    add_text_price = add_text*0.06 
    add_text_tax = float(add_text_price*(20/100))
    if add_minutes > 0:
        add_minutes_price=float(add_minutes*0.10,)
        add_minutes_tax=round(add_minutes_price*(20/100), 2)
        add_tax_all=round(add_minutes_tax + add_text_tax, 2)
        total_price= plan_price + add_minutes_price  + add_text_price + add_tax_all
        print(f'{add_text} additional messages for {add_text_price :.2f} levas')
        print(f'{add_minutes} additional minutes for {add_minutes_price :.2f} levas')
        print(f'{add_tax_all} additional taxes')
        print(f'{total_price} total bill')

    else:
        #nqma dop min
        total_price=float(add_text_price + add_text_tax + plan_price)
        print(f'{add_text} additional messages for {add_text_price :.2f} levas')
        print('0 additional minutes for 0.00 levas')
        print(f'{add_text_tax :.2f} additional taxes')
        print(f'{total_price :.2f} total bill')
else:
    if add_minutes > 0:
        # nqma dop sms
        add_minutes_price=round(add_minutes *0.10, 2)
        add_minutes_tax=round(add_minutes_price*(20/100), 2)
        total_price=float(plan_price+ add_minutes_price + add_minutes_tax)
        print("0 additional messages for 0.00 levas")
        print(f'{add_minutes} additional minutes for {add_minutes_price :.2f} levas')
        print(f'{add_minutes_tax :.2f} additional taxes')
        print(f'{total_price :.2f} total bill')
    else:
        #nqma dop min
        #nqma dop sms
        total_price=float(plan_price)
        print("0 additional messages for 0.00 levas")
        print("0 additional minutes for 0.00 levas")
        print("0.00 additional taxes")
        print(f'{plan_price :.2f} total bill')

