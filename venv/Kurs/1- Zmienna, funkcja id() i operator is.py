print(f'_____________________________')
print(f'Sekcja 1')
a = 20
b = 10
c = 10
print(f'{a} , {b} , {c}')
print(id(a),', ', id(b), ', ', id(c))

print(f'_____________________________')
print(f'Sekcja 2')
a=b=c=[1,2,3]

print(a, b, c)
print(id(a), id(b), id(c))

a.append(4)

print(a, b, c)

print(id(a), id(b), id(c))

print(a[0], id(a[0]))
print(a[1], id(a[1]))
print(a[2], id(a[2]))


print(f'_____________________________')
print(f'Sekcja 3')

x = 10
y = 10 + 123456789 - 123456789
print(x, id(x))
print(y, id(y))
