cake_01 = {
'taste' : 'vanilia',
'glaze' : 'chocolade',
'text' : 'Happy Brithday',
'weight' : 0.7
}
cake_02 = {
'taste' : 'tee',
'glaze' : 'lemon',
'text' : 'Happy Python Coding',
'weight' : 1.3
}

def show_cake_info(aCake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(aCake['taste'], aCake['glaze'], aCake['text'], aCake['weight']))
cakes = [cake_02, cake_01]
for c in cakes:
    show_cake_info(c)
print('_'*10)
show_cake_info(cake_01)
show_cake_info(cake_02)
