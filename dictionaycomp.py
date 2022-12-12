names = ["Maria", "Gendalf", "Batman"]
profs = ['programmer', 'wizard', 'superhero']

my_dict ={}

for (key, value) in zip(names, profs):
    my_dict[key] = value
    
print(my_dict)

employee = ["Nati", "Natalia", "Sarai", "Adrian", "Ciprian"]

job = ["mecanic", "farmacista", "pictor", "inginer", "zidar"]

new_dict ={k:v for k, v in zip(employee, job)}


print(new_dict)