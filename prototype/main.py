from abc import ABCMeta, abstractmethod
import copy # biblioteca para o Prototype

class Cursos(metaclass = ABCMeta):
	def __init__(self):
		self.id = None
		self.nome = None
		self.abr = None
		self.grau = None
	
	def get_nome(self):
		return self.nome
	
	def get_grau(self):
		return self.grau
	
	def get_id(self):
		return self.id
	
	def set_id(self, sid):
		self.id = sid
	
	def clone(self):
		return copy.copy(self)

class ADS(Cursos):
	def __init__(self):
		super().__init__()
		self.nome = "Análise e Desenvolvimento de Sistemas"
		self.abr = "ADS"
		self.grau = "Tecnólogo"

class SI(Cursos):
	def __init__(self):
		super().__init__()
		self.nome = "Sistemas de Informação"
		self.abr = "SI"
		self.grau = "Bacharelado"

class ENG_X(Cursos):
	def __init__(self):
		super().__init__()
		self.nome = "Engenharia X"
		self.abr = "ENG X"
		self.grau = "Bacharelado"

class Cursos_Copia:
	cache = {}  # guardar informação
	
	@staticmethod
	def get_curso(sid):
		curso = Cursos_Copia.cache.get(sid)
		return curso.clone()
	
	@staticmethod
	def load():
		si = SI()
		si.set_id("1")
		Cursos_Copia.cache[si.get_id()] = si  # Armazena o objeto si em cache, na posição do id do si
		
		ads = ADS()
		ads.set_id("2")
		Cursos_Copia.cache[ads.get_id()] = ads # Armazena o objeto ads em cache[ads.get_id()]
		
		eng_x = ENG_X()
		eng_x.set_id("3")
		Cursos_Copia.cache[eng_x.get_id()] = eng_x

# O Python começa executando a partir daqui...
if __name__ == '__main__':
	Cursos_Copia.load()
	
	si = Cursos_Copia.get_curso("1")
	print(f'Nome do curso: {si.nome} ({si.abr}), grau acadêmico: {si.grau}.')
	
	ads = Cursos_Copia.get_curso("2")
	print(f'Nome do curso: {ads.get_nome()} ({ads.abr}), grau acadêmico: {ads.get_grau()}.')
	
	eng_x = Cursos_Copia.get_curso("3")
	print(f'Nome do curso: {eng_x.get_nome()} ({eng_x.abr}), grau acadêmico: {eng_x.get_grau()}.')

