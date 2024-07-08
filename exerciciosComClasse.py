import random

# 1-Classe Bola: Crie uma classe que modele uma bola:
#     Atributos: Cor, circunferência, material
#     Métodos: trocaCor e mostraCor

# class Bola:
#     def __init__(self, cor, circunferencia, material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material
#
#     def trocarCor(self, novaCor):
#         self.cor = novaCor
#
#     def mostrarCor(self):
#         print(f"Cor = {self.cor}")
#
# bola = Bola("branco", "1m", "plastico")
# bola.mostrarCor()
# bola.trocarCor("preto")
# bola.mostrarCor()

# 2-Classe Quadrado: Crie uma classe que modele um quadrado:
#     Atributos: Tamanho do lado
#     Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

# class Quadrado:
#     def __init__(self, tam_lado):
#         self.lado = tam_lado
#
#     def mudarValorLado(self, novo_lado):
#         self.lado = novo_lado
#
#     def retornarValorLado(self):
#         print(f"Lado = {self.lado}")
#
#     def calcularArea(self):
#         area = self.lado * self.lado
#         print(f"Área = {area}")
#
# quadrado = Quadrado(2)
# quadrado.retornarValorLado()
# quadrado.calcularArea()
# quadrado.mudarValorLado(3)
# quadrado.retornarValorLado()
# quadrado.calcularArea()

# 3-Classe Retangulo: Crie uma classe que modele um retangulo:
#    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
#    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

# class Retangulo:
#     def __init__(self, comprimento, largura):
#         self.comprimento = comprimento
#         self.largura = largura
#
#     def mudarValorDosLados(self, novo_comprimento, nova_largura):
#         self.comprimento = novo_comprimento
#         self.largura = nova_largura
#
#     def retornarValorDosLados(self):
#         valores = []
#         valores.append(self.comprimento)
#         valores.append(self.largura)
#         return valores
#
#     def calularArea(self):
#         area = self.comprimento * self.largura
#         return area
#
#     def calcularPerimetro(self):
#         perimetro = 2 * (self.comprimento + self.largura)
#         return perimetro
#
# print("Informe as medidas do local que deseja fazer o acabamento, em metros.")
# local_comprimento = float(input("Digite o comprimento do local: "))
# local_largura = float(input("Digite a largura do local: "))
# # print("\nInforme as medidas do piso que será utilizado, em metros.")
# piso_comprimento = 0.6 #float(input("Digite o comprimento do piso: "))
# piso_largura = 0.6 #float(input("Digite a largura do piso: "))
#
# local = Retangulo(local_comprimento, local_largura) # criação do objeto
# piso = Retangulo(piso_comprimento, piso_largura)
#
# quantidade_pisos_para_chao = 0
# quantidade_recortes = 0
# sobra_do_recorte = 0
# for i in local.retornarValorDosLados():
#     recorte = round(i % piso.comprimento, 2) # pegando o tamanho do recorte, quando houver
#     if recorte > 0: # se houver recorte
#         quantidade_recortes = quantidade_recortes + (round((local.comprimento / piso.comprimento)))
#         # a quantidade de recortes será a mesma quantidade de peças de uma fileira
#         recortes_por_peca = piso.largura / recorte
#         if recortes_por_peca >= 2: # cada peça pode ter no máximo dois recortes, por causa do corte de fábrica
#             recortes_por_peca = 2
#         else:
#             recortes_por_peca = 1
#         quantidade_pecas_para_recorte = round((quantidade_recortes / recortes_por_peca) + 0.4)
#         quantidade_pisos_para_chao = (quantidade_pisos_para_chao + (2 * round(i / piso.comprimento))
#                                       + quantidade_pecas_para_recorte)
#         # quantidade de pisos para o chão está contando as peças inteiras + as peças para fazer os recortes
#         #
#         sobra_do_recorte = sobra_do_recorte + ((piso.largura - (recortes_por_peca * recorte))
#                                                * quantidade_pecas_para_recorte)
#         # tamanho das sobras dos recortes que poderá ser utilizado nos rodapés,
#         # visto que os rodapés não exigem nenhum dos lados com corte de fábrica
#     else:
#         quantidade_pisos_para_chao = quantidade_pisos_para_chao + (2 * (i / piso.comprimento))
#
# quantidade_pisos_para_chao = round(quantidade_pisos_para_chao + 0.4)
#
# quantidade_rodapes = 0
# for i in local.retornarValorDosLados():
#     # só estamos contando rodapés inteiros, daria para economizar contando também os recortes do rodapé
#     quantidade_rodapes = quantidade_rodapes + (2 * (round(i / piso.comprimento) + 0.4))
#
# quantidade_rodapes_por_piso = piso.largura / 0.1
# # 0.1m = 10cm estamos adotando rodapés de 10cm de largura e contando quantos rodapés cada peça dará
#
# quantidade_pisos_para_rodape = round((quantidade_rodapes / quantidade_rodapes_por_piso) + 0.4)
# quantidade_rodapes_menos_sobra = quantidade_rodapes - (sobra_do_recorte / 0.1)
# # descontando da quantidade de peças, as sobras que guardamos do recortes
# quantidade_pisos_para_rodape_menos_sobras = round((quantidade_rodapes_menos_sobra / quantidade_rodapes_por_piso) + 0.4)
# if quantidade_pisos_para_rodape_menos_sobras < 0:
#     quantidade_pisos_para_rodape_menos_sobras = 0
#
# print(f"\nTamanho do Local = {local.calularArea()}m²\n"
#       f"Considerando o piso com peças de 60x60cm\n"
#       f"Quantidade de peças para o chão = {quantidade_pisos_para_chao:.2f}")
# print(f"Quantidade de rodapés = {round(quantidade_rodapes + 0.5):.2f}\n"
#       f"Quantidade de pisos para os rodapés = {quantidade_pisos_para_rodape:.2f}\n"
#       f"Quantidade de pisos para os rodapés\n "
#       f"descontado as sobras dos recortes = {quantidade_pisos_para_rodape_menos_sobras:.2f}")
# print(f"Quantidade total de peças, para a obra, {quantidade_pisos_para_chao + quantidade_pisos_para_rodape_menos_sobras:.2f}.")

# 4-Classe Pessoa: Crie uma classe que modele uma pessoa:
#    Atributos: nome, idade, peso e altura
#    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

# class Pessoa:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura
#
#     def envelhecer(self, nova_idade):
#         if self.idade >= 21:
#             if nova_idade >= self.idade:
#                 self.idade = nova_idade
#             else:
#                 print(f"A idade informada {nova_idade} é menor que a idade atual {self.idade} d@ {self.nome}.")
#         else:
#             print("Envelhecer chamou Crescer")
#             self.crescer(nova_idade)
#
#     def engordar(self, novo_peso):
#         if novo_peso > self.peso:
#             self.peso = novo_peso
#             print(f"{self.nome}, você ganhou {novo_peso - self.peso}kg.")
#         else:
#             self.emagrecer(novo_peso)
#
#     def emagrecer(self, novo_peso):
#         if novo_peso < self.peso:
#             self.peso = novo_peso
#             print(f"{self.nome}, você eliminou {self.peso -  novo_peso}kg.")
#         else:
#             self.engordar(novo_peso)
#
#     def crescer(self, nova_idade):
#         if self.idade < 21 and nova_idade >= self.idade:
#             # if nova_idade >= self.idade:
#             if nova_idade < 21:
#                 idade = nova_idade - self.idade
#                 self.altura = self.altura + (idade * 0.5)
#             # elif self.idade < 21:
#             else:
#                 idade = 20 - self.idade
#                 self.altura = self.altura + (idade * 0.5)
#             self.idade = nova_idade
#         else:
#             print("Crescer chamou Envelhecer")
#             self.envelhecer(nova_idade)
#
# pessoa = Pessoa("Luana", 32, 69, 164)
# pessoa2 = Pessoa("Ana", 15, 52, 156)
#
# print(pessoa.idade, pessoa.altura)
# pessoa.crescer(33)
# print(pessoa.idade, pessoa.altura)
#
# print(pessoa2.idade, pessoa2.altura)
# pessoa2.envelhecer(26)
# print(pessoa2.idade, pessoa2.altura)

# 5-Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.

# class ContaCorrente:
#     def __init__(self, num_conta, nome, saldo=0):
#         self.numero_da_conta = num_conta
#         self.nome_correntista = nome
#         self.saldo = saldo
#
#     def alterarNome(self, novo_nome):
#         self.nome_correntista = novo_nome
#         return self.nome_correntista
#
#     def depositar(self, valor):
#         if valor > 0:
#             self.saldo = self.saldo + valor
#             print(f"\nDepósito de R${valor:.2f} efetuado com sucesso!\n"
#                   f"Saldo atualizado = {self.saldo:.2f}")
#         else:
#             valor = 0
#             print("\nO valor do Depósito deve ser maior que zero!")
#         return valor
#
#     def sacar(self, valor):
#         if valor <= self.saldo:
#             if valor > 0:
#                 self.saldo = self.saldo - valor
#                 print(f"\nSaque de R${valor:.2f} efetuado com sucesso!\n"
#                       f"Saldo atualizado = R${self.saldo:.2f}")
#             else:
#                 valor = 0
#                 print("\nO valor do Saque deve ser maior que zero!")
#         else:
#             # valor = 0
#             print(f"\nSaldo insuficiênte para sacar R${valor:.2f}!\n"
#                   f"Seu saldo é = {self.saldo:.2f}")
#         return valor
#
# cliente = ContaCorrente(1234, "Luana")
# print(f"Nome d@ cliente: {cliente.nome_correntista}")
# print(f"Nome d@ cliente {cliente.nome_correntista} alterado para: {cliente.alterarNome("Analu")}")
# print(f"Saldo inicial da conta: R${cliente.saldo:.2f}")
# cliente.depositar(600)
# cliente.sacar(150)
# cliente.sacar(450)
# cliente.sacar(10)

# 6-Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self, canais=20, volune_max=100):
        self.lista_canais = []
        i = 1
        while len(self.lista_canais) < canais:
            self.lista_canais.append(i)
            i += 1
        self.volume_atual = 0
        self.volume_max = volune_max
        self.canal = self.lista_canais[random.randint(0, len(self.lista_canais)-1)]

    def alterarCanal(self, num_canal):
        if num_canal in self.lista_canais:
            self.canal = num_canal
        else:
            print(f"Canal {num_canal} fora da faixa de canais desta TV.\n"
                  f"Canais disponíveis:", end=" ")
            for i in self.lista_canais:
                print(i, end="  ")
            print()

    def alterarVolume(self, botao_volume, num_vezes_pressionado=1):
        if botao_volume == "+":
            if (self.volume_atual + num_vezes_pressionado) <= self.volume_max:
                self.volume_atual = self.volume_atual + num_vezes_pressionado
            else:
                self.volume_atual = self.volume_max
                # volume máximo atingido
        elif botao_volume == "-":
            if (self.volume_atual - num_vezes_pressionado) >= 0:
                self.volume_atual = self.volume_atual - num_vezes_pressionado
            else:
                self.volume_atual = 0
                # volume mínimo atingido
        else:
            print("O comando recebido não altera o volume da TV.")

tv = TV()
print(f"Canal: {tv.canal}\n"
      f"Volume: {tv.volume_atual}")
tv.alterarCanal(4)
tv.alterarVolume("+",101)
print(f"Canal: {tv.canal}\n"
      f"Volume: {tv.volume_atual}")
tv.alterarVolume("-",8)
tv.alterarCanal(21)
print(f"Canal: {tv.canal}\n"
      f"Volume: {tv.volume_atual}")
tv.alterarVolume("*")