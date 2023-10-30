import math, time
start = time.time()
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

stop = time.time()
diff = stop - start
results_list = []
