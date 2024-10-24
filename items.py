from constants import*

class Item:
    def __init__(self, name, tipo, efecto, valor):
        self.__name = name  # Encapsulamos el nombre
        self.__tipo = tipo  # Encapsulamos el tipo
        self.__efecto = efecto  # Encapsulamos el efecto
        self.__valor = valor  # Encapsulamos el valor

    # Getters y Setters para name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getters y Setters para tipo
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    # Getters y Setters para efecto
    def get_efecto(self):
        return self.__efecto

    def set_efecto(self, efecto):
        self.__efecto = efecto

    # Getters y Setters para valor
    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    # Método para usar el ítem
    def use(self, character):
        if self.get_efecto() == 'salud':
            character.set_life(character.get_life() + self.get_valor())
            print(f"{character.get_name()} ha usado {self.get_name()} y ha restaurado {self.get_valor()} puntos de salud.")
        else:
            # Utilizamos los métodos getter y setter para actualizar el atributo correspondiente del character
            if self.get_efecto() == 'strength':
                character.set_strength(character.get_strength() + self.get_valor())
            elif self.get_efecto() == 'intelligence':
                character.set_intelligence(character.get_intelligence() + self.get_valor())
            elif self.get_efecto() == 'defense':
                character.set_defense(character.get_defense() + self.get_valor())
            elif self.get_efecto() == 'agility':
                character.set_agility(character.get_agility() + self.get_valor())
            print(f"{character.get_name()} ha usado {self.get_name()} y su {self.get_efecto()} ha aumentado en {self.get_valor()} puntos.")
        
        if self.get_tipo() == 'consumible':
            print(f"{self.get_name()} ha sido consumido y desaparece.")

# Lista de ítems disponibles
items_disponibles = [
    Item("Poción de vida", "consumible", "salud", 20),            
    Item("Espada de Acero", "permanente", "strength", 5),
    Item("Elixir de Sabiduría", "consumible", "intelligence", 10),
    Item("Escudo de Hierro", "permanente", "defense", 5),
    Item("Anillo de agilidad", "permanente", "agility", 3)
]