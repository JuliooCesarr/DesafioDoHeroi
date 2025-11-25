
class Personagem:
    def _init_(self, nome, vida, forca):
        self.nome = nome
        self._vida = vida            
        self.vida_max = vida
        self.forca = forca
        self.inventario = Inventario() 
        self.arma = None

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > self.vida_max:
            self._vida = self.vida_max
        else:
            self._vida = valor

    def receber_dano(self, dano):  
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def atacar(self, alvo):  
        dano = self.forca
        if self.arma:
            dano += self.arma.poder
        print(f"{self.nome} causa {dano} de dano em {alvo.nome}")
        alvo.receber_dano(dano)

    def esta_vivo(self):  
        return self.vida > 0


class Guerreiro(Personagem):
    def atacar(self, alvo):
        dano = self.forca + (self.arma.poder if self.arma else 0)
        print(f"{self.nome} usa ataque de força! Causa {dano}")
        alvo.receber_dano(dano)


class Mago(Personagem):
    def _init_(self, nome, vida, forca, poder_magico):
        super()._init_(nome, vida, forca)
        self.poder_magico = poder_magico

    def atacar(self, alvo):  # Questão 18
        dano = self.forca + self.poder_magico + (self.arma.poder if self.arma else 0)
        print(f"{self.nome} lança bola de energia! Causa {dano}")
        alvo.receber_dano(dano)


class Arqueiro(Personagem):
    def _init_(self, nome, vida, forca, precisao):
        super()._init_(nome, vida, forca)
        self.precisao = precisao

    def atacar(self, alvo):  # Questão 18
        dano = self.forca + self.precisao + (self.arma.poder if self.arma else 0)
        print(f"{self.nome} dispara flecha precisa! Causa {dano}")
        alvo.receber_dano(dano)

class Inimigo(Personagem):
    def __init__(self, nome, vida, força, poder):
        super()._init_(nome, vida, força)
        self.poder = poder
    def atacar(self, ataque):
        self.ataque = ataque

Monstro = Inimigo("Dracula", 3000, 1000, "sangue_venenoso")
Monstro.atacar("dentada")

class Inventario:
    def _init_(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        if item in self.itens:
            self.itens.remove(item)


def usar_pocao(personagem, pocao):
    if pocao in personagem.inventario.itens:
        personagem.vida += pocao.cura
        personagem.inventario.remover(pocao)
        print(f"{personagem.nome} usou {pocao.nome} e curou {pocao.cura}. Vida atual: {personagem.vida}")


class FabricaMonstros:
    @staticmethod
    def goblin_padrao():
        return Monstro("Goblin", 30, 5)