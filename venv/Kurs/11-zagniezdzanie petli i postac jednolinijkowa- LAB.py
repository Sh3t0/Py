ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#second_elements = [tuple[1] for tuple in list_of_tuples]
routes = [ (start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [ (start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))


### warunek start < stop lub start > stop powoduje wyeliminowanie duplikujacych sie tupletów w liscie.
### Warunek porównuje kolejność alfabetyczną dwóch napisów
routes = [ (start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))



#print( ports_connections(a,b))
#print( ports_connections(b,a))
#print(ports_connections )
#print(ports_connections.reverse())
#print(ports_connections)
#print(dict(ports_connections))
#print(ports_connections[1])
#print(id(ports_connections))
#print(disct(enumerate(ports_connections)))

#for a,b in ports_connections:
    #print (a,b,'  ',b,a)

