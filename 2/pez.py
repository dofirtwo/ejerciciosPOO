from animal import Animal
class Pez(Animal):
    def __init__(self, peso):
        super().__init__(peso)
        
    def respirar(self):
        print(f"un {type(self).__name__} respirando")
        
    def nadar(self):
        print(f"un {type(self).__name__} Nadando")