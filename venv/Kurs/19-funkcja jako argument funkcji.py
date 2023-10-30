def double(x):
    return 2 *x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

func_list = [double,square,negative,div2]

def generate_values(func_name, number):
    value_list = []
    for x in number:
        value_list.append(func_name(x))

    return value_list

x_table = list(range(11))

for f in func_list:
    print(generate_values(f, x_table))

