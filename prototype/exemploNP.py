class ADS:
    def nome(self):
        return "Análise e Desenvolvimento de Sistemas"
    
    def grau(self):
        return "Tecnólogo"
    
    def __str__(self):
        return "ADS"

class SI:
    def nome(self):
        return "Sistemas de Informação"
    
    def grau(self):
        return "Bacharelado"
    
    def __str__(self):
        return "SI"

class ENG_X:
    def nome(self):
        return "Engenharia X"
    
    def grau(self):
        return "Bacharelado"
    
    def __str__(self):
        return "ENG X"

# O Python começa executando a partir daqui...
if __name__ == "__main__":
    ads = ADS()      # objeto para ADS
    si = SI()        # objeto para SI
    eng_x = ENG_X()  # objeto para engenharia qualquer
    
    print(f'Nome do curso: {ads.nome()} ({ads}). Grau acadêmico: {ads.grau()}')
    print(f'Nome do curso: {si.nome()} ({si}). Grau acadêmico: {si.grau()}')
    print(f'Nome do curso: {eng_x.nome()} ({eng_x}). Grau acadêmico: {eng_x.grau()}')
