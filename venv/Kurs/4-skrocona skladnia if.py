dayType = 1
weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass


DayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holyday'
print(DayDescription)

print('weekend') if dayType == 1 else print ('workday') if dayType == 2 else print('holyday')
 ###########################################################################
price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

print(price)    if bonus_granted else ''
 ###########################################################################
rating = 4

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')
# ten if dziala na zasadzie
# #1 print('very good') if rating == 5 LUB  #2 print('good') if rating == 4 #3 else print('weak')
# else jest swego rodzaju rodzielnikiem tych if-ow






