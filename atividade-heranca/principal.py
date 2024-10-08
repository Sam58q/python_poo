from animal import BaseAnimal,Mamifero,Reptil


animal1 = BaseAnimal("Cachorro",1)
animal1.exibirInfo()
animal1.som("Woof")
print("-"*50)

animal2 = BaseAnimal("Cobra",6)
animal2.exibirInfo()

print("-"*50)

animal3 = BaseAnimal("Gato",2)
animal3.exibirInfo()

print("-"*80)

mam1 = Mamifero("Vaca", 3)
mam1.exibirInfo()
mam1.alimentarFilhotes()

print("-"*50)

mam2 = Mamifero("Elefante", 6)
mam2.exibirInfo()
mam2.alimentarFilhotes()

print("-"*50)


mam3 = Mamifero("Macaco", 3)
mam3.exibirInfo()
mam3.alimentarFilhotes()

print("-"*80)

rep1 = Reptil("Cobra", 1)
rep1.exibirInfo()
rep1.mudarPele()

print("-"*50)

rep2 = Reptil("Lagarto", 2)
rep2.exibirInfo()
rep2.mudarPele()
print("-"*50)


rep3 = Reptil("Iguana", 4)
rep3.exibirInfo()
rep3.mudarPele()

print("-"*50)


