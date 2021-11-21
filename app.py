class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.nivel_fome = 50
        self.nivel_energia = 50

    def brincar(self, valor_):
        self.nivel_energia += valor_
        if self.nivel_energia > 100:
            self.nivel_energia = 100
        elif self.nivel_energia < 0:
            self.nivel_energia = 0

    def comer(self, valor):
        self.nivel_fome = self.nivel_fome + valor
        if self.nivel_fome > 100:
            self.nivel_fome = 100
        elif self.nivel_fome < 0:
            self.nivel_fome = 0
        return f'{self.nivel_fome}'

    def retornar_nivel_fome(self):
        return self.nivel_fome

    def retornar_nivel_energia(self):
        return self.nivel_energia



