from time import sleep
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f'numero: {self.numero} \ncpf: {self.cpf} \nsaldo: {self.saldo}\n')
    
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ('Nao existe saldo suficiente')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return('Transferencia Realizada')


def principal():
    c1 = Conta(1001,45738539433,'Joao',50) # objeto sendo instanciado
    c2 = Conta(1, 453, 'Hugo', 10) # outro objeto sendo instanciado
    c1.depositar(150)
    c1.gerar_extrato()
    sleep(1.5)
    print('agora iremos sacar 50 ......')
    sleep(1.5)
    saque = c1.sacar(50)
    print('gerando extrato ....')
    sleep(1.5)
    c1.gerar_extrato()
    print(f'o saque foi realizado? {saque}')
    sleep(2)
    print('Iremos realizar agora uma transferencia de 40 merreus para Hugo ....')
    sleep(2)
    c1.transfereValor(c2, 40)
    print(f'O saldo da c1 e: {c1.saldo}')
    print(f'O saldo da c2 e: {c2.saldo}')


if __name__ == '__main__':
    principal()