class Human:
    def __init__(self, nam, e_c, hair_color):
        self.name = nam
        self.eye_color = e_c
        self.hair_color = hair_color
        self.health = 100
        self.inebriation = 0

    def workout(self):
        self.health += 10
        return self

    def eat(self):
        self.health += 5
        return self
    
    def introduce(self):
        print(f"Hi, my name is {self.name}")
        return self

class Ninja(Human):
    def __init__(self, nam, e_c):
        super().__init__(nam, e_c, "none")
        self.is_enlightened = True

    def leap_tall_building(self):
        self.health -= 20
        return self

    def introduce(self):
        print(f"Hi, I'm a ninja named {self.name}")
        return self

my_human = Ninja("Wes", "blue")
other_human = Human("Channa", "brown", "purple")

my_human.leap_tall_building()
other_human.introduce()
# my_human.workout()
# print(my_human.health)

# print(other_human.health)

# my_human.introduce()
# other_human.introduce()

# superman = other_human

my_human.workout().eat().workout().eat()
print(my_human.health, my_human.is_enlightened)