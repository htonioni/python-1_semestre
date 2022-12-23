class Veiculo:
    def __init__(self, montadora, modelo, cor):
        self.montadora = montadora
        self.modelo = modelo
        self.cor = cor
    
    def capacidade_assentos(self, capacidade):
        print(f'A capacidade maxima de assentos do veículo {self.modelo} é {capacidade}')
    
    def printar(self):
        print(f'O seu carro da {self.montadora} é da cor {self.cor}')

class Ônibus(Veiculo):
    def capacidade_assentos(self, qntd=70):
        return super().capacidade_assentos(capacidade=70)

    


onibus_escolar = Ônibus('Scania', '1000D', 'Vermei')
onibus_escolar.printar()
onibus_escolar.capacidade_assentos()


