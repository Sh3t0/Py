from datetime import datetime


def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[
        0]  # minuty divmod zwraca dwa parametry pierwszy to wynik dzielenia , a drugi modulo [0] wyswietla pierwsza zwrocona wartosc a [1] drugą


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60 * 60)[0]  # godziny


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60 * 60 * 24)  # dni


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))
print('-' * 30)


def create_function(func_name='f_minutes', span='m'):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def {}(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(func_name, sec)
    exec(source, globals())
    return globals()[func_name]

func_list =  [('f_minutes', 'm'), ('f_hours', 'h'), ('f_days', 'd')]
print(func_list[0][0], func_list[0][1])
print(type(func_list[0][0]), type(func_list[0][1]))
f_minutes = create_function('f_minutes', 'm')
f_hours = create_function(func_list[1][0], func_list[1][1])
f_days = create_function(func_list[2][0], func_list[2][1])


print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
print('-' * 30)


"""
f_minutes = create_function('f_minutes', 'm')
f_hours = create_function('f_hours', 'h')
f_days = create_function('f_days', 'd')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
"""

