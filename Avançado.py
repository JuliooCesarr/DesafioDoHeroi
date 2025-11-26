from Intermediário import Personagem, Guerreiro, Mago, Arqueiro, Monstro

class GeradorPseudo:
    valor = 17 

    @staticmethod
    def gerar(limite):
        """
        Gera um pseudo-aleatório entre 1 e limite.
        Apenas multiplicações e resto (%),
        sem usar random.
        """
        GeradorPseudo.valor = (GeradorPseudo.valor * 37 + 11) % 104729
        return (GeradorPseudo.valor % limite) + 1

class Habilidade:
    def usar(self, usuario, alvo):
        raise NotImplementedError("A habilidade deve implementar o método usar().")

class AtaqueForte(Habilidade):
    def _init_(self, multiplicador=1.8):
        self.multiplicador = multiplicador

    def usar(self, usuario, alvo):
        base = usuario.forca
        if usuario.arma:
            base += usuario.arma.poder

        dano = int(base * self.multiplicador)
        dano += GeradorPseudo.gerar(5) - 1

        print(f"{usuario.nome} usa Ataque Forte em {alvo.nome} causando {dano}!")
        alvo.receber_dano(dano)


class BolaDeFogo(Habilidade):
    def _init_(self, poder=10):
        self.poder = poder

    def usar(self, usuario, alvo):
        magia = getattr(usuario, "poder_magico", None)
        if magia:
            dano = magia * 2
        else:
            dano = self.poder

        if usuario.arma:
            dano += usuario.arma.poder


        dano += GeradorPseudo.gerar(6)

        print(f"{usuario.nome} lança Bola de Fogo em {alvo.nome} causando {dano}!")
        alvo.receber_dano(dano)

class Dado:
    @staticmethod
    def rolar(lados=20):
        return GeradorPseudo.gerar(lados)

def variar_dano(dano_base, amplitude=4):
    """Retorna dano_base +/- variação (sem random)."""
    variacao = GeradorPseudo.gerar(amplitude * 2) - amplitude
    return dano_base + variacao

class Orc(Monstro):
    def _init_(self, nome="Orc", vida=60, dano=12, chance_critico=20):
        """
        chance_critico = porcentagem inteira (20 = 20%)
        """
        super()._init_(nome, vida, dano)
        self.chance_critico = chance_critico

    def atacar(self):
        rolagem = GeradorPseudo.gerar(100)
        critico = rolagem <= self.chance_critico

        dano = self.dano * (2 if critico else 1)

        if critico:
            print(f"{self.nome} desfere GOLPE CRÍTICO! Dano: {dano}")
        else:
            print(f"{self.nome} ataca causando {dano}")

        return dano

class Batalha:
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def lutar(self):
        atacante = self.a
        defensor = self.b
        turno = 1

        while atacante.esta_vivo() and defensor.esta_vivo():
            print(f"\n--- RODADA {turno} ---")
            dano_base = atacante.forca
            if atacante.arma:
                dano_base += atacante.arma.poder

            dano = variar_dano(dano_base)

            print(f"{atacante.nome} ataca {defensor.nome} causando {dano}")
            defensor.receber_dano(dano)

            if not defensor.esta_vivo():
                print(f"\n{defensor.nome} foi derrotado!")
                return atacante

            atacante, defensor = defensor, atacante
            turno += 1

        return atacante

def adicionar_sistema_habilidade(classe):
    def add_habilidade(self, habilidade):
        if not hasattr(self, "habilidades"):
            self.habilidades = []
        self.habilidades.append(habilidade)

    def usar_habilidade(self, indice, alvo):
        if not hasattr(self, "habilidades"):
            print(f"{self.nome} não possui habilidades.")
            return
        if indice < 0 or indice >= len(self.habilidades):
            print("Habilidade inválida.")
            return
        self.habilidades[indice].usar(self, alvo)

    setattr(classe, "adicionar_habilidade", add_habilidade)
    setattr(classe, "usar_habilidade", usar_habilidade)

adicionar_sistema_habilidade(Personagem)
adicionar_sistema_habilidade(Guerreiro)
adicionar_sistema_habilidade(Mago)
adicionar_sistema_habilidade(Arqueiro)

class BatalhaEquipes:
    def _init_(self, equipe_a, equipe_b):
        self.a = equipe_a
        self.b = equipe_b

    def _vivo(self, equipe):
        for p in equipe:
            if p.esta_vivo():
                return p
        return None

    def lutar(self):
        rodada = 1
        print("\n--- BATALHA EM EQUIPES ---")

        while self._vivo(self.a) and self._vivo(self.b):
            a = self._vivo(self.a)
            b = self._vivo(self.b)

            print(f"\n--- RODADA {rodada} ---")

            print(f"{a.nome} (A) ataca {b.nome} (B)")
            a.atacar(b)

            if not b.esta_vivo():
                print(f"{b.nome} caiu!")
                rodada += 1
                continue

            print(f"{b.nome} (B) ataca {a.nome} (A)")
            b.atacar(a)

            if not a.esta_vivo():
                print(f"{a.nome} caiu!")

            rodada += 1

        if self._vivo(self.a):
            print("\nEquipe A venceu!")
            return "Equipe A"
        else:
            print("\nEquipe B venceu!")
            return "Equipe B"