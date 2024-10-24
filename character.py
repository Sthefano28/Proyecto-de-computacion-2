import random

class Character:

    def __init__(self, name, strength, intelligence, defense, life, level, experience, agility, spell):
        self.__name = name
        self.__strength = strength
        self.__intelligence = intelligence
        self.__defense = defense
        self.__life = life
        self.__experience = experience   
        self.__level = level
        self.__agility = agility
        self.__spell = spell
#Atributos Privados: Se prefijan con un guion bajo (_) para indicar que no deben ser accedidos directamente desde fuera de la clase.
#Getters: Métodos que permiten obtener el valor de un atributo privado.
#Setters: Métodos que permiten modificar el valor de un atributo privado, con la opción de incluir validaciones.
    # Getters
    def get_name(self):
        return self.__name

    def get_strength(self):
        return self.__strength

    def get_intelligence(self):
        return self.__intelligence

    def get_defense(self):
        return self.__defense

    def get_life(self):
        return self.__life

    def get_experience(self):
        return self.__experience

    def get_level(self):
        return self.__level

    def get_agility(self):
        return self.__agility

    def get_spell(self):
        return self.__spell

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_strength(self, strength):
        self.__strength = strength

    def set_intelligence(self, intelligence):
        self.__intelligence = intelligence

    def set_defense(self, defense):
        self.__defense = defense

    def set_life(self, life):
        self.__life = life

    def set_experience(self, experience):
        self.__experience = experience

    def set_level(self, level):
        self.__level = level

    def set_agility(self, agility):
        self.__agility = agility

    def set_spell(self, spell):
        self.__spell = spell

    # Mostrar atributos
    def attributes(self):
        print(f"{self.get_name()}:")
        print(f"· Strength: {self.get_strength()}")
        print(f"· Intelligence: {self.get_intelligence()}")
        print(f"· Defense: {self.get_defense()}")
        print(f"· Life: {self.get_life()}")
        print(f"· Level: {self.get_level()}")
        print(f"· Experience: {self.get_experience()}")
        print(f"· Agility: {self.get_agility()}")
        print(f"· Spell: {self.get_spell()}")

    # Subir de nivel con setters
    def level_up_experience(self, strength, intelligence, defense, level, experience, agility, spell):
        self.set_strength(self.get_strength() + strength)
        self.set_intelligence(self.get_intelligence() + intelligence)
        self.set_defense(self.get_defense() + defense)
        self.set_level(self.get_level() + level)
        self.set_experience(self.get_experience() + experience)    
        self.set_agility(self.get_agility() + agility)
        self.set_spell(self.get_spell() + spell)

    # Ver si está vivo
    def is_alive(self):
        return self.get_life() > 0

    # Morir
    def to_die(self):
        self.set_life(0)
        print(f"{self.get_name()} ha muerto")

    # Calcular daño
    def damage(self, enemy):
        return self.get_strength() - enemy.get_defense()

    # Atacar
    def to_attack(self, enemy):

        damage = self.damage(enemy)
        
        enemy.set_life(enemy.get_life() - damage)

        print(f"{self.get_name()} ha realizado {damage} puntos de daño a {enemy.get_name()}")

        if enemy.is_alive():
            print(f"{enemy.get_name()} está vivo")
        else:
            enemy.to_die()

    # Usar objeto
    def use_item(self, item):
        item.use(self)

        
