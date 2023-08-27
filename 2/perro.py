from animal import Animal
class Perro(Animal):
    def __init__(self, peso):
        super().__init__(peso)
        
    def respirar(self):
        print(f"un {type(self).__name__} respirando")
        
    def ladrar(self):
        print(f"un {type(self).__name__} Ladrando")