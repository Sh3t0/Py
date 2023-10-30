ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#second_elements = [tuple[1] for tuple in list_of_tuples]
routes = [ (start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))


routes_gen = ( (start, stop) for start in ports for stop in ports if start != stop and start < stop)
print(routes_gen)
#print(len(routes_gen))

i=0
while True:
    try:
        print(next(routes_gen))
        i+=1
    except StopIteration:
        print('All done!', i)
        break

