class Veiculo:
    def __init__(self, nome, vel_max, km_litro):
        self.nome = nome
        self.vel_max = vel_max
        self.km_litro = km_litro

    def printar(self):
        print(f'O seu carro é: {self.nome}\nTem a velocidade maxima de: {self.vel_max}\nKm/litro de: {self.km_litro}')


modelo_carro = Veiculo('Fusca', 120, 8)
modelo_carro.printar()