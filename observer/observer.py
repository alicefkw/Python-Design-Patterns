
class Assinante:
    def __init__(self, name):
        self.name = name
    
    def notificar(self, msg):
        print(f'{self.name} foi notificado(a)! Mensagem: "{msg}".')
    
class Publicador:
    def __init__(self):
        self.assinantes = set()
    
    def cadastrar(self, pessoa):
        self.assinantes.add(pessoa)
    
    def descadastrar(self, pessoa):
        self.assinantes.discard(pessoa)
    
    def enviar(self, msg):
        for assinante in self.assinantes:
            assinante.notificar(msg)