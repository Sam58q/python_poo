from funcionario import Funcionario

Funcionario1 = Funcionario("Gerente",3000)
print("Seu cargo atual é :",Funcionario1.getCargo())

Funcionario1.cargo = "Supervisor"# Acessando o atributo direto
Funcionario1.setCargo("Engenheiro")#Acessando o método para mudar o cargo
print("Seu cargo atual é :",Funcionario1.getCargo())

# Exibindo o salário
print("O seu salário atual é", Funcionario1.salario)

Funcionario1.salario = 5500
print("O seu salário atual é", Funcionario1.salario)