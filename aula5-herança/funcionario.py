class Funcionario: #super-classe ou classe-mãe
    def __init__(self,nome,cargo):
        # Estamos mudando a visiblidade do atributo de privado para protegido,dessa forma, as classes filhas poderão acessar os atributos da classe mãe.
        self._nome = nome 
        self._cargo = cargo
        
        
    def informacoes(self):
        print(f"Olá {self._nome}, na empresa seu cargo é: {self._cargo}")

#Criando classe filha 
class Engenheiro(Funcionario):# A classe engenheiro está herdando as características da classe Funcionario, que será sua mãe 
    def monstrarDetalhes(self):
        print(f"olá,eu sou{self._nome} e sou um engenheiro")
        
        
class Secretario(Funcionario):
    def relatorio(self):
        print(f"Olá seu cargo é {self._cargo}")
    