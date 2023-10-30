from datetime import datetime
import time
import functools

def wrapper_time(a_function):# dekorator
    def a_wrapper_func(*args, **kwargs):# opakowanie funkcji
        time_start = datetime.now()
        v = a_function(*args, **kwargs)
        time_stop = datetime.now()
        duration = time_stop - time_start
        print("Funkcja {} wykonana w czasie {}".format(a_function.__name__, duration))
        return v
    return a_wrapper_func

@wrapper_time# wywołanie dekoratora
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v




#print(get_sequence(19))

#diff = end - start

#duration_in_s = duration.total_seconds()
#print(diff)
print('-'*30)
"""wrapper_get_sequence = wrapper_time(get_sequence)
print('>', wrapper_time(3))
print('>>', a_wrapper_func(get_sequence))
print('>>>', wrapper_get_sequence(5))#prawidlowe wypisanie"""
print(get_sequence(3))
