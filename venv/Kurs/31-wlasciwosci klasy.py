import pickle
import glob

class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []
    #path = r'c:\temp\piekarnia.bakery'

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        #isinstance(obiekt, typ)
        if isinstance(additives, str):
            self.additives = additives
        else:
            self.additives = additives.copy()
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)
        #print(self.bakery_offer)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(cake01, f)
        f.close()
    @classmethod #metoda klasy
    def read_from_file(cls, path):#cls - class bo pracujemy na poziomie klasy, SELF- występuje na poziomie instacji[obiektów]
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        print(cls.bakery_offer)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        print(glob.glob(path))#zwaraca liste plikow z zadanym rozszerzeniem
        return glob.glob(path)

    text = property(__get_text, __set_text, None, 'Text on the cake')

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], '', False, '')
cake03 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [], '', True, 'Good Night')
cake04 = Cake('Cocoa Waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')
#cake01.__gluten_free = True # w ten sposob nie mozna zmienic wartosci w klasie
cake01._Cake__gluten_free = True# automatycznie utworzony atrybut klasy pozwala zmienic wartosc w klasie
cake01._Cake__set_text('Dla matuli i dla starego')
#cake01.__text = 'Dla matuli i dla starego'

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake01.save_to_file(r'c:\temp\piekarnia.cake01.bakery')
cake02.save_to_file(r'c:\temp\piekarnia.cake02.bakery')
cake05 = Cake.read_from_file(r'c:\temp\piekarnia.cake01.bakery')
print(Cake.read_from_file(r'c:\temp\piekarnia.cake01.bakery'))
print('x'*10)
cake05.show_info()
#cake01._Cake__get_text()
Cake.get_bakery_files(r'c:\temp\*.bakery')

print(dir(cake01))
print(vars(cake01))
