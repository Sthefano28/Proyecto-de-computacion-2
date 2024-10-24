import random

class Challenge:
    
    def __init__(self, description, difficulty):
        self.__description = description  # Encapsulamos description
        self.__difficulty = difficulty  # Encapsulamos difficulty

    # Getters y Setters para description
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    # Getters y Setters para difficulty
    def get_difficulty(self):
        return self.__difficulty

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    # Método para resolver el desafío
    def to_solve(self, character):
        print(f"{character.get_name()} enfrenta un desafío: {self.get_description()}")
        # Simular resolución de desafío
        exit = random.randint(0, 10) > self.get_difficulty()

        if exit:
            print(f"{character.get_name()} ha superado el desafío!")
        else:
            print(f"{character.get_name()} ha fallado el desafío...")

        return exit