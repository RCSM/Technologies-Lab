# Criar formas de bebidas e seus dados serem globais
# Criar funcionamento mais interessante para o bar
# Corrigir : funciona compilado em pytho3 mas nao no pypy

from random import randint

class Estoque():
    def __init__(self, qtde_pessoas):
        if qtde_pessoas > 50:
            print("Muita gente, vai faltar bebida")
        else:
            print("Bebidas que restaram da noite : ", 50-qtde_pessoas)

class Bar():
    def __init__(self, qtde_pessoas):
        Estoque.__init__(self, qtde_pessoas)
        self.qtde_barmans = qtde_pessoas/15
        self.barmans = []
        for i in range(round(self.qtde_barmans)):
            self.barmans.append(Barman())
            self.barmans[i].str_oi()
            self.barmans[i].atender_pedidos()

        
class Pessoa():
    _grana_gasta = 0

    def __init__(self, tipo):
        if tipo == "consumidor":
            self.estilo = "casual"
            self.grana = 120

    def gastar_tudo(self):
        self._grana_gasta = self.grana
        return self._grana_gasta

    def gasta_metade(self):
        self._grana_gasta = self.grana/2
        return self._grana_gasta

class Barman(Pessoa):
    _pedido = {"bebida" : "", "valor" : 0}

    def __init__(self):
        Pessoa.__init__(self, "barman") # Inutil
        self.qtde_pessoas_atendidas = 0

    def atender_pedidos(self):
        self.lotacao = []
        self._pedido["bebida"] = "cerveja"
        self._pedido["valor"] = 12
        for l in range(15):
            self.lotacao.append(Pessoa("consumidor"))
            print(self._pedido)
        print("Barman lotado\n+++++++++\n")

    def str_oi(self):
        print("Oi, sou um barman")

######################################

def main():
    # Testes do bar    
    b = Bar(42)

    # Testes de pessoa
#    p = Pessoa("consumidor")
#    print(p.gastar_tudo())
#    print(p.gasta_metade())

    # Testes de barman
#    b = Barman()
#    print(b.atender_pedido())

    # Testes para o estoque
#    e = Estoque(50)

if __name__ == '__main__':
    main()
