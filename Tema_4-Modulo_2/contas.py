import datetime
from c_extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor 
        self.extrato.transacoes.append(["DEPOSITO", valor, "data",datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ('Saldo insuficiente')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return ('Transferencia Realizada')

    def gerarSaldo(self):
        print(f'O saldo da conta {self.numero} e de {self.saldo}')