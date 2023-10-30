

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)

print(f(text_list[3]))
print('-'*30)
#print(len(text_list))
for i in range(len(text_list)):
    print(f(text_list[i]))

print('-'*30)

print(list(map(f,text_list))) # funkcja map map, pozwala uruchomić wskazywaną przez pierwszy argument funkcję dla listy przekazanej jako drugi argument.


print(list(map(lambda s: len(s),text_list))) #dynamiczne definiowanie



