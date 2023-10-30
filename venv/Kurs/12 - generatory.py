listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)

product = [(a,b) for a in listA for b in listB]
print(product)

product = [    (a,b) for a in listA for b in listB if a%2 ==1 and b%2 == 0  ]
print(product)

product = {    a:b for a in listA for b in listB if a%2 ==1 and b%2 == 0  }
print(product)
#generatory wykorzystuje sie do masowych danych
gen = (    (a,b) for a in listA for b in listB if a%2 ==1 and b%2 == 0  )
print(next(gen))
print(next(gen))
print('_'*40)
for x in gen:
    print(x)
print('-'*40)
for x in gen:
    print(x)


print('+'*40)
gen = (    (a,b) for a in listA for b in listB if a%2 ==1 and b%2 == 0  )
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all done!')
        break
