varX = 10
passwd = 'P4ssw0rD_1'
source = 'varX+3'
# import biblioteki plikow. get current working directory CWD
source2 = '__import__("os").getcwd()'

#varGlobals = globals().copy()
varGlobals = {}
#del varGlobals['passwd']
#eval pozwala na wywolanie kodu z zewnatrz, bazy danych, pliku etc. wadą jest to ze mozna tym namieszać w kodzie źródłowym
result = eval(source, globals())
print(result)
#print(varGlobals)
#print(globals())

