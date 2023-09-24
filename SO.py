class Bloco:
    def __init__(self, data):
        self.data = data
        self.proximo = None

class GA:
    def __init__(self, tamanho):
        self.disco = [None] * tamanho
        self.tamanho = tamanho
        self.espacoLivre = tamanho

    def criar(self, palavra):
        espaco_necessario = len(palavra) * tambloc
        if espaco_necessario > self.espacoLivre:
            print("Espaço insuficiente.")
            return

        bloco_atual = 0
        for caractere in palavra:
           while bloco_atual < self.tamanho:
                bloco = self.disco[bloco_atual]
                if bloco is None:
                    bloco = Bloco(caractere)
                    self.disco[bloco_atual] = bloco
                    self.espacoLivre -= tambloc
                    break
                bloco_atual += 1

    def excluir(self, palavra):
        for i in range(self.tamanho):
            bloco = self.disco[i]
            if bloco is not None and bloco.data == palavra[0]:
                j = 0
                while j < len(palavra):
                    if self.disco[i + j] is None or self.disco[i + j].data != palavra[j]:
                        break
                    j += 1
                if j == len(palavra):
                    for j in range(len(palavra)):
                        self.disco[i + j] = None

    def imprimir(self):
        for i in range(self.tamanho):
            bloco = self.disco[i]
            if bloco is not None:
                print(f"Bloco {i}: {bloco.data}")
            else:
                print(f"Bloco {i}: Livre")


tambloc = 1
disco = GA(32)
disco.criar("Pernambuco")
print("ADD: Pernambuco")
disco.imprimir()
disco.criar("Sao Paulo")
print("ADD: Sao Paulo")
disco.imprimir()
disco.criar("Alagoas")
print("ADD: Alagoas")
disco.imprimir()
disco.criar("Santa Catarina")
print("ADD: Santa Catarina")
disco.imprimir()
print("Excluir: Sao Paulo")
disco.excluir("Sao Paulo")
disco.imprimir()
disco.criar("Santa Catarina")
print("ADD: Santa Catarina")
disco.imprimir()
