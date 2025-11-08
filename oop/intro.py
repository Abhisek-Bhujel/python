class Kettle:
    power_source = 'electricity'
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
        
    def switch_on(self):
        self.on = True
        
    def switch_off(self):
        self.on = False


kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

hamilton = Kettle("hamilton", 15.55)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print('*' * 80)

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print('*' * 80)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_off()
print(kenwood.on)
print('*' * 80)

#unlike java we can add attribute and methods after creating object from class
kenwood.power = 1.5
print(kenwood.power)

#gives error
#print(hamilton.power)

#power_source is electricity
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print('*' * 80)

#switch power_source to atomic
Kettle.power_source = 'atomic'
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print('*' * 80)

#switch kenwood power_source to gas
kenwood.power_source ='gas'
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)