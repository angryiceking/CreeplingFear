class Item():

    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(
                                                self.name,
                                                self.desc,
                                                self.value)

class Gold(Item):

    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                        desc="Main currency",
                        value=self.amt)
    def get_value(self):
        return self.amt

class Weapon(Item):

    def __init__(self, name, desc, value, damage):
        self.damage = damage
        super().__init__(name, desc, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(
                                                self.name,
                                                self.desc,
                                                self.value,
                                                self.damage)
class Rock(Weapon):

    def __init__(self):
        super().__init__(name="Rock",
                        desc="A tiny rock",
                        value=0,
                        damage=5)

class Dagger(Weapon):

    def __init__(self):
        super().__init__(name="Dagger",
                        desc="Made from kitchen knife",
                        value=5,
                        damage=10)
