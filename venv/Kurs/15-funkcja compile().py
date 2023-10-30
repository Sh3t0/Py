import time
source = "reportLine += 1"
reportLine = 0
#______________________________________
start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start
print(time_not_compiled)
#______________________________________
#compile(co skompilowac - fragment tekstu, źródło np plik tekstowy z ktorego czytamy lub zmienna lub randomowy tekst, tryb[mode] eval/exec/simple  wyrazenie/kod/pojedyncza instrukcja
sourceCompile = compile(source,'internal variable source', 'exec')
#exec(sourceCompile)
#print(reportLine)

#______________________________________
start = time.time()
for i in range(100000):
    exec(sourceCompile)
stop = time.time()
time_compiled = stop - start
print(time_compiled)
#______________________________________
print(time_not_compiled/time_compiled)
