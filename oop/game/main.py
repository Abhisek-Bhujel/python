from player import Player
from enemy import Enemy, Troll, Vampire

tim = Player("Tim")

random_enemy = Enemy("Basic enemy", 12, 1)
print(random_enemy)

random_enemy.take_damage(4)
print(random_enemy)

random_enemy.take_damage(10)
print(random_enemy)

ugly_troll = Troll("Ugly_Troll")
print(ugly_troll)

ugly_troll.stomp()

dracula = Vampire('dracula')
print(dracula)

dracula.take_damage(5)
print(dracula)




