from animal import Animal
class Gato(Animal):
    def __init__(self, peso):
        super().__init__(peso)
    
    def respirar(self):
        print(f"un {type(self).__name__} respirando")
    
    def maullar(self):
        print(f"un {type(self).__name__} Maullado")
    