from character import Character
from constants import*
class Warrior(Character):
    
    def __init__(self, name, strength=50, intelligence=10, defense=25, life=100, level=1, experience=50, agility=0, spell=0, sword=1):
        super().__init__(name, strength, intelligence, defense, life, level, experience, agility, spell)
        self.__sword = sword  # Encapsulamos sword

    # Getter y Setter para sword
    def get_sword(self):
        return self.__sword

    def set_sword(self, sword):
        self.__sword = sword

    # Sobreescribir el método attributes
    def attributes(self):
        super().attributes()
        print(f"· Sword: {self.get_sword()}")

    # Sobreescribir el método damage
    def damage(self, enemy):
        option = int(input(DAMAGE_WARRIOR_OPTION))# DAMAGE_WARRIOR_OPTION
        
        if option == 1:
            self.set_sword(80)  # Modificamos la espada con el setter
            self.set_strength(50)  # Usamos el setter para strength
            
        elif option == 2:
            self.set_sword(10)
            self.set_strength(20)
        else:
            print(OPTION_WARRIOR)  # Manejamos el error para opciones inválidas
        
        # Calculamos el daño utilizando getters para acceder a los atributos
        return (self.get_strength() + self.get_sword()) - enemy.get_defense() + self.get_life()

    # Setters y getters adicionales heredados de Character
    def set_strength(self, strength):
        super().set_strength(strength)

    def get_strength(self):
        return super().get_strength()