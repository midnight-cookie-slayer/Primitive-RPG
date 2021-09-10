import random
class Warrior:
    def __init__(self, name, hp, damage, mana):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
    def __str__(self):
        str = ''
        str += 'Воин: ' + self.name + '\n'
        return str
    def giving_damage(self, object):
        object.hp -= self.damage
        print(object.name + ': ' + str(object.hp))
        if object.hp <= 0:
            print(object.name + 'умер от руки ' + self.name)

class Bow:
    def __init__(self, name, hp, damage, mana):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
    def __str__(self):
        str = ''
        str += 'Лучник: ' + self.name + '\n'
        return str
    def giving_damage(self, object):
        object.hp -= random.randint(0, self.damage)
        print(object.name + ': ' + str(object.hp))
        if object.hp <= 0:
            print(object.name + 'умер от метких выстрелов ' + self.name)

class Mag:
    def __init__(self, name, hp, damage, mana):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
    def __str__(self):
        str = ''
        str += 'Маг: ' + self.name + '\n'
        return str