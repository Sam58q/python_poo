class Funcionario:
    def __init__(self, nome, cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def exibirDados(self):
        print(f"Bom dia {self.nome} seu cargo é {self.cargo} e o salário {self.salario}.") 
    def verificarSalario(self):
        Salario = self.salario
        if Salario <= 2000:
            print("Sem direito a bonus")
        else:
            print("Você tem direito a bonus")
