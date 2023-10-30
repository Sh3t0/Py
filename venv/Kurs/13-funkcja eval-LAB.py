import math
#ecal wykonuje pojedyncze wyrazenie
n = 10  # wartość górna zakresu
step = 0.1  # krok iteracji

arg_list = []
lista = [round(x * step,1) for x in range(int(n/step) + 1)]
formula = input('Wprowadź wzór funkcji: ') # 2*x

for x in lista:
    print(eval(formula))

""" 
# lepsze rozwiazanie problemu
import math
 
argument_list = []
 
for i in range (100):
    argument_list.append(i/10)
    
formula = input("Please enter a formula, use 'x' as the argument: ")
 
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))
    
"""

