lst1 = list()
lst2 = list()
dct = dict()

while True:
    m = input("Introduceti legume: ")
    n = input("Introduce culoarea: ")
    if m and n == "q":
        break
    lst1.append(m)
    lst2.append(n)
    dct = {k:v for k, v in zip(lst1, lst2)}
    
print(dct)

k = input("Valoare: ")
q = 0

for item in lst2:
    if k == item:
        q +=1
print(q)

# print(help(dct))