class Animal():
    def __init__(self,peso):
        self.__peso=peso
        
    def getPeso(self):
        return self.__peso
    
    def setPeso(self,peso):
        self.__peso=peso
        
    def respirar(self):
        print(f"un {type(self).__name__} respirando")