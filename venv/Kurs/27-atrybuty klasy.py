class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        #atrybuty klasy
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

#instancje
cake_apple = Cake('Apple Cake','Sweet', 'Sweet Apple', 'Apples', 'Cream')
cake_pear = Cake('Pear Cake', 'Medium Sweet', 'Medium Pear', 'None', 'None')
cake_peach = Cake('Peach Cake', 'Low Sweet', 'Low Peach', 'Parts of fruit', 'None')

#lista
bakery_offer = [cake_peach, cake_apple, cake_pear]

for b in bakery_offer:
    print("{} - {} cake with main taste: {}  with addition of {} and {}". format(b.name, b.kind, b.taste, b.additives, b.filling))
