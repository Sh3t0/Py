projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
# The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...
for p,l in zip(projects,leaders):
    print('The leader of',p,"is",l)


dates = ['2016-06-23', '2016-08-29', '1994-01-01']
#The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
for p,l,d in zip(projects,leaders,dates):
    print('The leader of',p,'started',d,"is",l)


#...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
for pos,(p,l,d) in enumerate(zip(projects,leaders,dates)):
    print('Position:',pos,'- The leader of',p,'started',d,"is",l)


"""for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))"""
