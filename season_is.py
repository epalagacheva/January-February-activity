month=input()
date=int(input())

if  date  <=1 and  date >=31:
    print("Not valid date")
else:
    if month == "March":
        if date >=20 and date <=31:
            print ("Spring")
    elif month=="April" or month=="May":
        print ("Spring")
    elif month=="June":
        if date >=1 and date <=20:
            print ("Spring")

    if month == "June":
        if date >=21 and date <=30:
            print ("Summer")
    elif month=="July" or month=="August":
        print ("Summer")
    elif month=="September":
        if date >=1 and date <=21:
            print ("Summer")
    if month == "September":
        if date >=22 and date <=30:
            print ("Autumn")
    elif month=="October" or month=="November":
        print ("Autumn")
    elif month=="December":
        if date >=1 and date <=20:
            print ("Autumn")
    if month == "December":
        if date >=21 and date <=31:
            print ("Winter")
    elif month=="January" or month=="February":
        print ("Winter")
    elif month=="March":
        if date >=1 and date <=19:
            print ("Summer")
    
    

    


