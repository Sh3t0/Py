varX = 10
source = 'varX = 3'
source2 = '''
            new_var = 1
            for i in range(varX):
                print('-'*i)
                new_var +=1
          '''


result = exec(source2)
print(result)
print(varX)
print(new_var)


source = input("Enter expression: ")
print(eval(source))
