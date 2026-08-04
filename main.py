from models.Funcionario import Funcionario
from models.Setor import Setor

s1 = Setor(1, "TI")
f1 = Funcionario(1, "Rafael", "Dev", 4000, s1)

f1.aumentar_salario(1000)
f1.mostrar_dados()
print("")
# s1.nome = "Metrologia"
# s1.apresentar

#devolve erro
#s1.nome = ""






















#COMPOSIÇÃO
#funcionário possui um setor
#produto possui um fornecedor
#produto pertence a um setor
#HERANÇA
#Gerente é um funcionário
#Supervisor é um funcionário
#ADM é um funcionário



# print(f1.get_id())
# print(f1.get_nome())
# print(f1.get_cargo())
# print(f1.get_salario())
# f1.set_nome("Ivan")
# f1.set_cargo("Diretor")
# f1.set_salario(8350)
# f1.mostrar_dados()


# f1.mostrar_dados()
# print(f1.nome)
# print(f1.salario)
# f1.salario = 7000
# f1.cargo = "Dev Sênior"
# f1.mostrar_dados()