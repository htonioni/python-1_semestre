from contas import Conta
from cliente import Cliente
from time import sleep
cliente1 = Cliente(467, 'Hugo', 'Carlos Gomes')
cliente2 = Cliente(813, 'Monica', 'Muniz')
conta1 = Conta([cliente1, cliente2], 1, 1500)
conta1.gerarSaldo()
print(f'Depositando R$257 na conta 1 ....\n')
sleep(1.5)
conta1.depositar(257)
conta1.depositar(100)
conta1.sacar(600)
print(f'Agora sacamos 600 para restar 1157....')
sleep(1.5)
conta1.gerarSaldo()
print(f'O endereco do cliente 1 eh: {cliente1.endereco}')
conta1.extrato.extrato(conta1.numero)