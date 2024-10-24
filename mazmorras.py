from combat import *
from challenge import *



class Mazmorra:
    def __init__(self, name, enemys, boss):
        self.__name = name  # Encapsulamos name
        self.__enemys = enemys  # Encapsulamos enemys (lista)
        self.__boss = boss  # Encapsulamos boss
        self.__challenges = []  # Encapsulamos la lista de desafíos

    # Getter y Setter para name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter y Setter para enemys
    def get_enemys(self):
        return self.__enemys

    def set_enemys(self, enemys):
        self.__enemys = enemys

    # Getter y Setter para boss
    def get_boss(self):
        return self.__boss

    def set_boss(self, boss):
        self.__boss = boss

    # Getter y Setter para challenges
    def get_challenges(self):
        return self.__challenges

    def set_challenges(self, challenges):
        self.__challenges = challenges

    # Método para añadir desafíos
    def add_challenges(self, challenge):
        self.__challenges.append(challenge)

    # Método para explorar la mazmorra
    def explorare(self, character):
        print(f"\n{character.get_name()} entra en la mazmorra {self.get_name()}...\n")
        
        # Luchar contra los enemys
        for enemy in self.get_enemys():
            combat(character, enemy)
            if not character.is_alive():
                print(f"{character.get_name()} ha sido derrotado en la mazmorra {self.get_name()}...")
                return False  # El personaje murió en la mazmorra
        
        # Resolver desafíos
        for challenge in self.get_challenges():
            turn = 0
            if not challenge.to_solve(character):
                print(f"{character.get_name()} no pudo resolver el desafío y fue derrotado.")
                turn += 1
                print(f"Turno {turn}")
                return False
        
        # Luchar contra el boss
        print(f"\n{character.get_name()} se enfrenta al boss de la mazmorra {self.get_name()}: {self.get_boss().get_name()}\n")
        
        combat(character, self.get_boss())
        if character.is_alive():
            print(f"{character.get_name()} ha conquistado la mazmorra {self.get_name()}!\n")
            return True
        else:
            print(f"{character.get_name()} ha sido derrotado por el boss {self.get_boss().get_name()}.")
            return False