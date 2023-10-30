import os
#exec wykonuje duza ilosc kodu

script1 = r'E:\Kurs Python\2.Rozbudowa kodu\14-funkcja exec\skrypt1.txt'
script2 = r'E:\Kurs Python\2.Rozbudowa kodu\14-funkcja exec\skrypt2.txt'

print(script1)

with open(script1,'r') as file:
    content_script_1 = file.read()
    #print(content_script_1)

with open(script2,'r') as file:
    content_script_2 = file.read()
    #print(content_script_2)


exec(content_script_1)
exec(content_script_2)
