class Aduanre():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def adunare(a,b):
        print(a+b)
        
adun = Aduanre.adunare(5,6)



class Persoane():
    def __init__(self,nume,prenume,adresa):
        self.nume = nume
        self.prenume = prenume
        self.adresa = adresa
        
    def afisare(nume,prenume,adresa):
        print(nume + "\n" + prenume + "\n" + adresa)


persoana  = Persoane.afisare("Hordon ", "Natanael", "Zăbrani")

class Dreptunghi():
    def __init__(self,lungime, latime):
        self.lungine = lungime
        self.latime = latime

    def arie(lungime, latime):
        print(lungime*latime)
        
        
class Patrat(Dreptunghi):
    def __init__(self,lungime):
        super.__arie__(lungime,lungime)
a = Patrat.arie(3,6)



