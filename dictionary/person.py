class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # def __getattr__(self, attr):
    #     if attr in ['_name', '_age']:  # Sprawdzenie, czy atrybut należy do listy chronionych atrybutów
    #         print("first")
    #         return getattr(self, attr)  # Wywołanie wbudowanej funkcji getattr dla chronionych atrybutów
    #     else:
    #         print("firste")
    #         raise AttributeError(f"'Person' objectggggg has no attribute '{attr}'")

    # def __getattribute__(self, attr):
    #     if attr in ['_name', '_age']:  # Sprawdzenie, czy atrybut należy do listy chronionych atrybutów
    #         print("second")
    #         return object.__getattribute__(self, attr)
    #     else:
    #         print("seconde")
    #         raise AttributeError(f"'Person' objectggggg has no attribute '{attr}'")


p = Person("Mariusz", 90)
print(p.dupa)