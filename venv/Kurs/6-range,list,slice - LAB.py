

def colors (color_list,n):
    #color_list = color_list.copy()
    print(color_list[0:n])

def colors_in_loop(color_list):
    print('All posible lists: ')
    for i in range(1,len(color_list)+1):
        print(color_list[0:i])

color_range = 3#int(input('Insert range of colors:'))
color_list = ["red", "orange", "green", "violet", "blue", "yellow"]
#print(color_list[0:2])
colors(color_list,color_range)
print ('_' * 40)
colors_in_loop(color_list)

print('No. of elements in list: ',(len(color_list)))
print ('_' * 40)

tekst = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
#print ( tekst.split('(') )
#print ( tekst.split(')') )
nr_otwarcia = 0
nr_zamkniecia = 0
j = 0
#while iteruje po indeksach tekstu
while j < len(tekst):
    #print(j,len(tekst))
    if tekst[j] == "(":
        nr_otwarcia = j+1
    if tekst[j] == ")":
        nr_zamkniecia = j
    j+=1
else:
    print ('While',nr_otwarcia, nr_zamkniecia)
# for iteruje po literach tekstu
'''for i in (tekst):

    if i == "(":
        nr_otwarcia = i
    if i == ")":
        nr_zamkniecia = i
else:
    print (nr_otwarcia, nr_zamkniecia)'''

teskt_cutted = tekst[nr_otwarcia:nr_zamkniecia]

print(teskt_cutted)

#wyswietlnie tekstu od:do - PROSCIEJ
print(tekst[tekst.index('(')+1 : tekst.index(')')])
