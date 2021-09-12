import random


class Warrior:
    def __init__(self, name, hp, damage, mana, luck):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.luck = luck

    def __str__(self):
        str = ''
        str += 'Воин: ' + self.name + '\n'
        return str

    def giving_damage(self, object):
        object.hp -= random.randint(0, self.luck) * self.damage
        print(object.name + ': ' + str(object.hp))
        if object.hp <= 0:
            print(object.name + ' погиб от руки ' + self.name)


class Bow:
    def __init__(self, name, hp, damage, mana, luck):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.luck = luck    #luck should be no more than 45% (1.45)
        """if luck > 45 and luck <= 0:
            print('Некорректные параметры удачи!')    #don't like this way
            exit()"""

    def __str__(self):
        str = ''
        str += 'Лучник: ' + self.name + '\n'
        return str

    def giving_damage(self, object):
        object.hp -= random.randint(0, self.luck) * self.damage
        print(object.name + ': ' + str(object.hp))
        if object.hp <= 0:
            print(object.name + ' умер от метких выстрелов ' + self.name)


class Mag:
    def __init__(self, name, hp, damage, mana, luck):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.luck = luck    #luck should be no more than 25% (1.25)

    def __str__(self):
        str = ''
        str += 'Маг: ' + self.name + '\n'
        return str

    def giving_damage(self, object):
        if self.mana <= 0:
            print('У мага ' + self.name + ' не осталось маны, поэтому ему придётся продолжать битву посохом')
            self.damage = 5
        object.hp -= random.randint(0, self.luck) * self.damage
        self.mana -= 15
        if object.hp <= 0:
            print(object.name + ' был испепелён великим ' + self.name)