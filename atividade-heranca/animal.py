class BaseAnimal:
    def __init__(self,nome,idade):
        self._nome = nome 
        self._idade = idade
    def exibirInfo(self):
        print(f"O Nome: {self._nome} e Idade: {self._idade} ")
        
    def som(self,tipoSom):
        print(f"Este animal faz o som: {tipoSom} ")
        
class Mamifero(BaseAnimal):
    def alimentarFilhotes(self):
        print(f"O mamifero: {self._nome} está alimentando seus filhotes ")
        
        
class Reptil(BaseAnimal):
    def mudarPele(self):
        print(f"O reptil: {self._nome} está mudando de pele")