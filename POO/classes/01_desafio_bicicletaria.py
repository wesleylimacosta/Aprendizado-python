class Bicicleta:
    cor: str;
    modelo: str;
    ano: int;
    valor: float;
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor;
        self.modelo = modelo;
        self.ano = ano;
        self.valor = valor;
        
        
    def buzinar(self):
        print('bi bi');
    
    def empinar(self):
        print('Empinando...');
    
    def frear(self):
        print('Freando...');
        
    def pedalar(self):
        print('Peladando...');
        
    # def __str__(self):
    #     return f'Bicicleta {self.cor}, {self.modelo}, {self.ano}, {self.valor}'
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"
    

b1 = Bicicleta('vermelha', 'caloi', 2020, 1000, 26);
b2 = Bicicleta('azul', 'monark', 2021, 2000, 29);

print(b1);
print(b2);
