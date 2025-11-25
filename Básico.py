
class Guerreiro:
    def __init__(self, nome, vida, forca, arma):
        self.nome = nome
        self.vida = vida
        self.forca = forca  
        self.arma = None

    def atacar(self, ataque):
        self.ataque = ataque + Espada_longa.dano

    def equipar(self, equipe):
        self.equipe = equipe

Guerreiro_peso= Guerreiro("cleitin da paz", 2000, 1500)
Guerreiro_peso.atacar("lapada_seca")
Guerreiro_peso.equipar("Espada_longa")

print(f"{Guerreiro_peso.nome} tem {Guerreiro_peso.vida} de vida")
                        
class Mago:
    def __init__(self, nome, magia, vida, ação):
        self.nome = nome
        self.magia = magia
        self.vida = vida
        self.ação = ação

    def atacar(self, ataque):
        self.ataque = ataque

Mago_peso = Mago("Chavoso", "fogo", 800)
Mago_peso.atacar("bola_de_fogo")

print(f"O mago {Mago_peso.nome} tem o poder de {Mago_peso.magia} e tem {Mago_peso.vida} de vida")

class Arqueiro:
    def __init__(self, nome, precisão, vida):
        self.nome = nome
        self.precisão = precisão
        self.vida = vida

    def atacar(self, ataque):
        self.ataque = ataque

Arqueiro_peso = Arqueiro("Trevoso", 90, 1000)
Arqueiro_peso.atacar("flechada_mistica")

print(f"O Arqueiro {Arqueiro_peso.nome} tem uma precisão de {Arqueiro_peso.precisão} porcento e sua vida é de {Arqueiro_peso.vida}")

class Inimigo:
    def __init__(self, nome, vida, força, poder):
        self.nome = nome
        self.vida = vida
        self.força = força
        self.poder = poder

    def atacar(self, ataque):
        self.ataque = ataque

Monstro = Inimigo("Dracula", 3000, 1000, "sangue_venenoso")
Monstro.atacar("dentada")

print(f"O {Monstro.nome} é um temido vilão, sua vida de {Monstro.vida} e sua {Monstro.poder} no pescoço são de arrepiar")
        
class Armas:
    def __init__(self, nome, alcance, dano, tipo):
        self.nome = nome
        self.alcance = alcance
        self.dano = dano
        self.tipo = tipo

Cajado_mágico = Armas("cajado mágico", "longo", 300, "mágica")

Espada_longa = Armas("espada longa", "curto", 400, "corpo a corpo")

class poção:
    def __init__(self, nome, valor_de_cura):
        self.nome = nome
        self.valor_de_cura = valor_de_cura

Poção1 = poção("cura_cura", 50)