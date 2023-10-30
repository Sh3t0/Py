import os
#funkcja zliczająca slowa
def count_words(path_to_file):
    with open(path_to_file,'r') as file:
        content = file.read()
        words = content.split()#mozna okreslic separator np. ';' ',' '.' itd
        words_count = len(words)
    return words_count





path = r'c:\temp\data.txt'
if os.path.isfile(path):
    os.remove(path)

#dlugie tworzenie pliku
'''
if os.path.isfile(path):
    print('File %s exists' % path)
    print('File', path, 'exists')

else:
    print('Creating a file %s' % path)
    open(path, 'x').close()
    print('File %s created' % path)
'''
#krotkie tworzneie pliku
if os.path.isfile(path):
    os.remove(path)
result = os.path.isfile(path) or open(path,'x').close()
print(result)
'''
with open(path, 'w') as plik: #pisanie do pliku w-rite
        tekst = 'Jakiś tekst który wpisany zostanie do pliku'
        plik.write(tekst)
'''
with open(path, 'a') as plik: #dopisywanie do pliku a-ppend
    tekst = 'Linia 1\nLinia 2 - Jakiś tekst który wpisany zostanie do pliku\nLinia2\nLinia3\nLinia4'
    plik.write(tekst)

print(count_words(path))

