class ClasseSomaSubtrai:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def somar(self):
        return self.x + self.y
    
    def subtrair(self):
        return self.x - self.y

class SubClassMultDiv(ClasseSomaSubtrai):
    def multi(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y


soma = ClasseSomaSubtrai(15, 5)
print(f'A soma entre {soma.x} e {soma.y} é {soma.somar()}')
        
div = SubClassMultDiv(30, 2)
print(f'A divisao entre {div.x} e {div.y} é {div.div():.0f}')