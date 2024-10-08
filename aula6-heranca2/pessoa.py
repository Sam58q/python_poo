class Pessoa: #superclass ou classe mãe
    def __init__(self,nome,idade):
        self._nome = nome 
        self._idade = idade
        
    def info(self):
        print(f"Nome : {self._nome}. idade: {self._idade}")
    
#Classe filha 1 - aluno 
class Aluno(Pessoa):
    def __init__(self,nome,idade,serie):
        super().__init__(nome,idade)#utilizando o construtor da classe mãe
        self._serie = serie # Estamos utilizando um atributo exclusivo da classe filha 
    def estudar(self):
        print(f"{self._nome}, está na estudando na seríe {self._serie}")

#Class filha 2 - Professor
class Professor(Pessoa):
    def __init__(self, nome, idade,disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina
    def ensinar(self):
        print(f"{self._nome}, professor(a) da disciplina {self._disciplina}, está ensinando")
    
        