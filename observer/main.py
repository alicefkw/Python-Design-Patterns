from observer import Publicador, Assinante

pub = Publicador()

a = Assinante('A')
b = Assinante('B')
c = Assinante('C')
d = Assinante('D')
e = Assinante('E')
f = Assinante('F')

pub.cadastrar(a)
pub.cadastrar(b)
pub.cadastrar(c)
pub.cadastrar(d)
pub.cadastrar(e)
pub.cadastrar(f)

pub.enviar("Fofoca 1")

pub.descadastrar(b)

print("\n---b descadastrado---\n")

pub.enviar("Fofoca 2")