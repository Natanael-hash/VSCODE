angajat = {"nume": "Hordon", "prenume": "Natanael", "salariu": 2000}
print(angajat)
# print(dir(angajat))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# print(help(angajat.update))

d = {"email": angajat["nume"].lower() + "." + angajat["prenume"].lower() + "@company.com", "telefon": "111.222.333"}
angajat.update(d)
print(angajat)