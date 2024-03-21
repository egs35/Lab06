# Define the Character class
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Define the Hero class, inheriting from Character
class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.weapon = None

    def equip(self, weapon):
        self.weapon = weapon

# Define the Enemy class, inheriting from Character
class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

# Define the Weapon class
class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

# Create weapon instances
empty_handed = Weapon(name="Empty handed", weapon_type="dummy", damage=0, value=0)
healing_staff = Weapon(name="Healing Staff", weapon_type="magic", damage=-3, value=0)

# Create character instances
protagonist = Hero(name="Hero", health=100)
protagonist.health = 10  # Adjusting health as per instruction
protagonist.equip(empty_handed)

ally = Enemy(name="Friendly Enemy", health=100, weapon=healing_staff)

# Example of a simple game loop or interaction
print(f"{protagonist.name} is equipped with {protagonist.weapon.name}.")
print(f"{ally.name} is equipped with {ally.weapon.name}.")
