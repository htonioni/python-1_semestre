class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus

class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agreagado = salario
    def salario_total(self):
        return self.salario_agreagado.salario_anual()

salario = Salario(2000, 157)
employee = Empregado('Hugo', 22, salario)
print(f'O novo salario de {employee.nome} é:',employee.salario_total())

