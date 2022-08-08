class calculadora:
    
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    
    def soma(self):
        resultado = self.a + self.b
        self.impressao(resultado)
        
    def subtração (self):
        resultado = self.a - self.b
        self.impressao(resultado)
        
    def impressao(self, c):
        print(c)
        