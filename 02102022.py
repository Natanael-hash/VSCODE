# a = [1, 'ceva', True, 5.2] 

# b = a[0]

# print(len(a))

# a.append("doi")
# a.append("trei")

# print(a[2:])
# print(a[:5])
# print(dir(a))

# m = range(5)

# print(m)

# m = list(m)

# print(m)

# e = {"rosu": 1, "alb": 2}

# print(e["alb"])

# lst = list()

# lst.append("Silvia")
# lst.append("Sara")
# lst.append("Beatrice")

# print(lst)

# # print(dir(lst))

# for item in lst:
#     print(item)


lst1 = list()

while True:
    a = input("Scrieti: ")
    if a == "q":
        break
    lst1.append(a)

v = input("Nume: ")
c = 0
for item in lst1:
    if v == item:
        c += 1
print(c)


            




