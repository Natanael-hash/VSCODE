import math 
lst = [item*3 for item in range(11)]
print(lst)

lst1 =[item for item in range(101) if item %2 ==1]
print(lst1)

lst_of_languages = ['   romana   ', ' germana ', '    engleza    ', 'poloneza ', '  chineza  ']
new_lst_of_languages = [language.strip() for language in lst_of_languages]

print(new_lst_of_languages)

persoane = [('Bogdan', 14), ('Ana',20), ('Marius',18), ('Ionut',30), ('Claudia',12), ('Adrian',10)]

varsta = [persoana[0] for persoana in persoane if persoana[1] >= 18]
print(varsta)

lst3 = [item for item in range(1001) if int(math.sqrt(item)) == math.sqrt(item)]

print(lst3)

