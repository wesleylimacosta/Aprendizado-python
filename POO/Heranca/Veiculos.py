class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        print('O veículo está ligado')

    def desligar(self):
        print('O veículo está desligado')

    def acelerar(self):
        print('O veículo está acelerando')

    def frear(self):
        print('O veículo está freiando')

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, portas):
        super().__init__(marca, modelo, ano, cor)
        self.portas = portas

    def abrir_porta(self):
        print('Porta aberta')

    def fechar_porta(self):
        print('Porta fechada')

    def __str__(self):
        return f'Carro: {super().__str__()}, Portas: {self.portas}'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, cilindradas):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
        
    def empinar(self):
        print('Empinando...')
    
    def __str__(self):
        return f'Moto: {super().__str__()}, Cilindradas: {self.cilindradas}'


c1 = Carro('Ford', 'Fiesta', 2019, 'Preto', 4)
m1 = Moto('Honda', 'Biz', 2020, 'Vermelha', 125)
print("Carro:")
c1.ligar()
c1.acelerar()
c1.frear()
c1.desligar()
print("\n")
print("Moto:")
m1.ligar()
m1.acelerar()
m1.frear()
m1.desligar()
m1.empinar()