from funcionario import Funcionario,Engenheiro,Secretario

f1 = Funcionario("Joana","Gerente")
eng1 = Engenheiro("Robertp","Engenheiro") 
sec1 = Secretario("Marco","Secretario")

f1.informacoes()

eng1.informacoes()
eng1.monstrarDetalhes()

Secretario.relatorio()