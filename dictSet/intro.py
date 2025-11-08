vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jinny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']
print(my_car)

learner = vehicles.get("er5")
print(learner)

print("*" * 50)

for key in vehicles:
    print(key, vehicles[key], sep=": ")

print("*" * 50)

vehicles["toy"] = "Glider"

for key, value in vehicles.items():
    print(key,value, sep=": ")
    
#Update the virago
vehicles['virago'] = 'Yamaha XV535'

for key, value in vehicles.items():
    print(key,value, sep=": ")
 
print("*" * 50)
 
#deleting from dictionary
del vehicles['virago']   

for key, value in vehicles.items():
    print(key,value, sep=": ")