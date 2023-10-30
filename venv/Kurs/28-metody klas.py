class Cake:
    def __init__(self, name, kind, taste, additives=[], filling=None):
        #atrybuty klasy
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives = []
        self.filling = filling
        #self.show_info = show_info
        #self.set_filling = set_filling
        #self.add_additives = add_additives

        #motoda klasy


    def set_filling(self, filling):
        self.filling = filling


    def add_additives(self, new_additives = []):
        self.additives = []
        for c in new_additives:
            self.additives.append(c)



    def show_info(self):
        print(self.name.upper())
        print('Kind: ', self.kind)
        print('Taste: ', self.taste)
        if self.filling:
            print('Filling: ', self.filling)
        else:
            pass
            #print('Filling: ', self.filling)
        if self.additives:
            print('Additives:', end=' ')
            for additive in self.additives:
                print(additive, end=', ')
            print()



#instancje
cake_apple = Cake('Apple Cake','Sweet', 'Sweet Apple', 'Apples')
cake_pear = Cake('Pear Cake', 'Medium Sweet', 'Medium Pear')
cake_peach = Cake('Peach Cake', 'Low Sweet', 'Low Peach', 'Parts of fruit')
#cake_apple.set_filling('Cream')
#lista
bakery_offer = ['Sugar', 'Chockolate']

cake_apple.add_additives(bakery_offer)
cake_apple.show_info()

