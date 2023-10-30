banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
banknotes_nominates = ['1gr','2gr','5gr','10gr','50gr','1zl','2zl','5zl','10zl','20zl','50zl','100zl','200zl','500zl']
denomination = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_denominations = dict(zip(banknotes_coins,denomination))
print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1
   #print('File %s exists' % path)
for coins in dict_denominations:
    #print(f'Denominate:  {format(coins,5,3)} - amount  {dict_denominations[coins]}')
    print('Denominate: %6.2f  - amount  %d'% (coins,dict_denominations[coins]) )
