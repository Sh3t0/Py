for i in range(1,5): # od 1 do 4
    print (i)
print ('_' * 40)

for i in range(5): # od 0 do 4
    print (i)
print ('_' * 40)

for i in range(1,11,2): #co 2
    print (i)
print ('_' * 40)


for i in range(10,0,-1): #od 10 do 1, kazda iteracja o -1
    print (i)
print ('_' * 40)


#list = range(0,10)
#print('List: ',list,type(list))

list = list(range(0,10))
print('List: ',list,type(list))

print(list)
print(list[-1::-1]) #element ostatni [5:8] od 5 do 7 itd, [5:-1] od 5 do ostatniego
print(list[-1:0:-1])
#for i in list:
#   print(list[i])


