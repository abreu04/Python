import datetime
import math
# 1-Faça um Programa que peça dois números e imprima o maior deles

# numero_1 = float(input("Digite o primeiro número: "))
# numero_2 = float(input("Digite o segundo número: "))
# if numero_1 > numero_2:
#     print(f"O maior digitado foi {numero_1}.")
# else:
#     print(f"O maior digitado foi {numero_2}.")

# 2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

# valor = float(input("Digite um número positivo ou negativo: "))
# if valor > 0:
#     print("O número digitado é positivo!")
# elif valor < 0:
#     print("O número digitado é negativo!")
# else:
#     print("O valor digitado é zero!")

# 3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

# sexo = input("Informe o sexo. Digite F para meninino e M para masculino: ")
# sexo = sexo.upper()
# if "F" == sexo:
#     print("F - Feminino.")
# elif "M" == sexo:
#     print("M - Masculino.")
# else:
#     print("Sexo inválido.")

# 4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante

# vogais = ["a", "e", "i", "o", "u"]
# consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z"]
# letra = input("Digite uma letra: ")
# if letra in vogais:
#     print("A letra digitada é uma vogal!")
# elif letra in consoantes:
#     print("A letra digitada é uma consoante!")
# else:
#     print("O item digitado não é uma letra do alfabeto brasileiro!")

# 5-Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
#     A mensagem "Reprovado", se a média for menor do que sete
#     A mensagem "Aprovado com Distinção", se a média for igual a dez

# notas = []
# for i in range(2):
#     nota = float(input(f"Digite a nota {i+1}: "))
#     notas.append(nota)
# media = sum(notas) / 2
# if media == 10:
#     print("Aprovado com Distição!")
# elif media >= 7:
#     print("Aprovado!")
# elif media < 7:
#     print("Reprovado :(")

# 6-Faça um Programa que leia três números e mostre o maior deles

# maior = 0
# for i in range(3):
#     numero = float(input(f"Digite o número {i+1}: "))
#     if i == 0:
#         maior = numero
#     if numero > maior:
#         maior = numero
# print(f"O maior número digitado foi {maior}.")

# 7-Faça um Programa que leia três números e mostre o maior e o menor deles

# maior = 0
# menor = 0
# for i in range(3):
#     numero = float(input(f"Digite o número {i+1}: "))
#     if i == 0:
#         maior = numero
#         menor = numero
#     if numero > maior:
#         maior = numero
#     if numero < menor:
#         menor = numero
# print(f"O maior número digitado foi {maior}. \nE o menor número digitado foi {menor}.")

# 8-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato

# produtos = {"Arroz": 0, "Farinha": 0, "Milho": 0}
# menor_preco = 0
# mais_barato = ""
# for produto in produtos:
#     produtos[produto] = float(input(f"Informe o preço do {produto}: "))
#     if produto == "Arroz":
#         menor_preco = produtos[produto]
#         mais_barato = produto
#     if menor_preco > produtos[produto]:
#         menor_preco = produtos[produto]
#         mais_barato = produto
# print(f"{mais_barato} é o produto menos caro da lista, custando R${menor_preco}.")

# 9-Faça um Programa que leia três números e mostre-os em ordem decrescente

# numeros = []
# for i in range(3):
#     numero = float(input(f"Digite o número {i+1}: "))
#     numeros.append(numero)
# print(f"Lista na ordem digitada: {numeros}")
# numeros.sort(reverse=True)
# print(f"Lista em ordem decrescente: {numeros}")

# 10-Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

# turno = input("Qual turno você estuda? \nDigite M para Matutino, V para Vespertino ou N para Noturno: ")
# turno = turno.upper()
# if turno == "M":
#     print("Bom dia")
# elif turno == "V":
#     print("Boa tarde!")
# elif turno == "N":
#     print("Boa noite!")
# else:
#     print("Valor inválido!")

# 11-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculará os reajustes.
#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

# salario_atual = float(input("Digite o salário: "))
# salario_novo = 0
# if salario_atual <= 280:
#     salario_novo = salario_atual * 1.2
#     print(f"Salário antes do reajuste R${salario_atual}."
#           f"\nPercentual do reajuste 20%."
#           f"\nValor do aumento R${round(salario_novo-salario_atual,2)}."
#           f"\nSalário reajustado R${round(salario_novo,2)}")
# elif salario_atual > 280 and salario_atual <= 700:
#     salario_novo = salario_atual * 1.15
#     print(f"Salário antes do reajuste R${salario_atual}."
#           f"\nPercentual do reajuste 15%."
#           f"\nValor do aumento R${round(salario_novo-salario_atual,2)}."
#           f"\nSalário reajustado R${round(salario_novo,2)}")
# elif salario_atual > 700 and salario_atual < 1500:
#     salario_novo = salario_atual * 1.1
#     print(f"Salário antes do reajuste R${salario_atual}."
#           f"\nPercentual do reajuste 10%."
#           f"\nValor do aumento R${round(salario_novo-salario_atual,2)}."
#           f"\nSalário reajustado R${round(salario_novo,2)}")
# else:
#     salario_novo = salario_atual * 1.05
#     print(f"Salário antes do reajuste R${salario_atual}."
#           f"\nPercentual do reajuste 5%."
#           f"\nValor do aumento R${round(salario_novo-salario_atual,2)}."
#           f"\nSalário reajustado R${round(salario_novo,2)}")

# 12-Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo), 10% do INSS e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20%
#     Imprima na tela as informações, salário bruto, valor e percentual do IR, do INSS, do sindicato e do FGTS
#     Imprima também o total de descontos e o salário líquido

# valor_hora = float(input("Informe o valor da sua hora trabalhada: "))
# horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))
# salario_bruto = valor_hora * horas_trabalhadas
# inss = salario_bruto * 0.1
# sindicato = salario_bruto * 0.03
# fgts = salario_bruto * 0.11
# if salario_bruto <= 900:
#     ir = 0
#     ir_p = 0
# elif salario_bruto > 900 and salario_bruto <= 1500:
#     ir = salario_bruto * 0.05
#     ir_p = 5
# elif salario_bruto > 1500 and salario_bruto <= 2500:
#     ir = salario_bruto * 0.1
#     ir_p = 10
# else:
#     ir = salario_bruto * 0.2
#     ir_p = 20
# descontos = inss + sindicato + ir
# salario_liquido = salario_bruto - descontos
# print(f"\t\tSalário Bruto: ({valor_hora} * {horas_trabalhadas})"
#       f"\n: R$ {salario_bruto}"
#       f"\n\t\t\t\t\t (-)   IR   ({ir_p}%)"
#       f"\n: R$  {ir}"
#       f"\n\t\t\t\t  (-)   INSS   ( 10%)"
#       f"\n: R$  {inss}"
#       f"\n\t\t\t\t\t    FGTS   ( 11%)"
#       f"\n: R$  {fgts}"
#       f"\n\t\t\t\t   Total de descontos"
#       f"\n: R$  {descontos}"
#       f"\n\t\t\t\t\t  Salário Líquido"
#       f"\n: R$ {salario_liquido}")

# 13-Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido

# semana = {1:"Domingo", 2:"Segunda", 3:"Terça", 4:"Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
# chave = int(input("Escolha o dia da semana digitando um número inteiro de 1 a 7,\nsendo que 1 corresponde a Domingo: "))
# if chave >= 1 and chave <= 7:
#     print(semana[chave])
# else:
#     print("Valor inválido!")

# 14-Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#       Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E

# notas = []
# for i in range(2):
#     nota = float(input(f"Digite a nota {i+1}: "))
#     notas.append(nota)
# media = sum(notas) / len(notas)
# if media >= 9 and media <= 10:
#     print(f"Média: {media} => Conceito: A => Aprovado")
# elif media >= 7.5 and media < 9:
#     print(f"Média: {media} => Conceito: B => Aprovado")
# elif media >= 6 and media < 7.5:
#     print(f"Média: {media} => Conceito: C => Aprovado")
# elif media >= 4 and media < 6:
#     print(f"Média: {media} => Conceito: D => Reprovado")
# elif media >= 0 and media < 4:
#     print(f"Média: {media} => Conceito: E => Reprovado")
# else:
#     print("Esta média encontra-se fora dos padrões estabelecidos.")

# 15-Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro
#     Triângulo Equilátero: três lados iguais
#     Triângulo Isósceles: quaisquer dois lados iguais
#     Triângulo Escaleno: três lados diferentes

# medidas = []
# for i in range(3):
#     lado = float(input(f"Digite a medida do lado {i+1}: "))
#     medidas.append(lado)
# dois_lados = medidas[0] + medidas [1]
# if dois_lados > medidas[2]:
#     if medidas[0] == medidas[1] and medidas[0] == medidas[2]:
#         print("As medidas são de um triângulo equilátero, três lados iguais.")
#     elif medidas[0] == medidas[1] or medidas[0] == medidas[2] or medidas[1] == medidas[2]:
#         print("As medidas são de um triângulo isósceles, dois lados iguais.")
#     else:
#         print("As medidas são de um triângulo escaleno, três lados diferentes.")
# else:
#     print("As medidas informadas não formam um triângulo.")

# 16-Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações
#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
#     o programa não deve pedir os demais valores, sendo encerrado
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário

# valores = []
# for i in range(3):
#     valor = float(input(f"Digite o valor {i+1}: "))
#     if i == 0 and valor == 0:
#         print("O valor a deve ser diferente de zero, do contrário não é equação de segundo grau.")
#         break
#     else:
#         valores.append(valor)
# delta = (valores[1] * valores[1]) - (4 * valores[0] * valores[2])
# if delta < 0:
#     print("O valor de delta é negativo. A equação não possui raizes reais.")
# elif delta == 0:
#     raiz_unica = -(valores[1]) / (2 * valores[0])
#     print(f"Delta igual a zero, por isso há somente uma raiz = {raiz_unica}.")
# else:
#     raiz_1 = (-(valores[1]) + (math.sqrt(delta))) / (2 * valores[0])
#     raiz_2 = (-(valores[1]) - (math.sqrt(delta))) / (2 * valores[0])
#     print(f"O valor de delta é positivo, e ad raizes são {round(raiz_1,2)} e {round(raiz_2,2)}.")

# 17-Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

# ano = int(input("Digite um número correspondente a um ano: "))
# x = ano % 4
# if x > 0:
#     print(f"O ano {ano} não é bissexto,")
# else:
#     print(f"O ano {ano} é bissexto!")

# 18-Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

# data = input(f"Digite um data com o seguinte formato dd/mm/aaaa: ")
# print(data)
# dia_s = len(data[:2])
# dia = int(data[:2])
# mes_s = len(data[3:5])
# mes = int(data[3:5])
# ano_s = len(data[6:])
# ano = int(data[6:])
# if dia > 0 and dia <= 31 and dia_s == 2:
#     if mes > 0 and mes <= 12 and mes_s == 2:
#         if ano > 0 and ano_s == 4:
#             print(f"Data válida: {data}.")
#         else:
#             print("Data inválida, ano fora do padrão esperado.")
#     else:
#         print("Data inválida, mês fora do padrão esperado.")
# else:
#     print("Data inválida, dia fora do padrão esperado.")

# 19-Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo
#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# def imprima (numero):
#     centena = int(numero / 100)
#     numero = numero % 100
#     dezena = int(numero / 10)
#     numero = numero % 10
#     unidade = numero
#     if centena == 0:
#         if dezena == 0:
#             if unidade == 0:
#                 print("Não há centena, dezena ou unidade para ser exibida.")
#             elif unidade == 1:
#                 print(f"{num} = {unidade} unidade")
#             else:
#                 print(f"{num} = {unidade} unidades")
#         elif dezena == 1:
#             if unidade == 0:
#                 print(f"{num} = {dezena} dezena")
#             elif unidade == 1:
#                 print(f"{num} = {dezena} dezena e {unidade} unidade")
#             else:
#                 print(f"{num} = {dezena} dezena e {unidade} unidades")
#         else:
#             if unidade == 0:
#                 print(f"{num} = {dezena} dezenas")
#             elif unidade == 1:
#                 print(f"{num} = {dezena} dezenas e {unidade} unidade")
#             else:
#                 print(f"{num} = {dezena} dezenas e {unidade} unidades")
#     elif centena == 1:
#         if dezena == 0:
#             if unidade == 0:
#                 print(f"{num} = {centena} centena")
#             elif unidade == 1:
#                 print(f"{num} = {centena} centena e {unidade} unidade")
#             else:
#                 print(f"{num} = {centena} centena e {unidade} unidades")
#         elif dezena == 1:
#             if unidade == 0:
#                 print(f"{num} = {centena} centena e {dezena} dezena")
#             elif unidade == 1:
#                 print(f"{num} = {centena} centena, {dezena} dezena e {unidade} unidade")
#             else:
#                 print(f"{num} = {centena} centena, {dezena} dezena e {unidade} unidades")
#         else:
#             if unidade == 0:
#                 print(f"{num} = {centena} centena e {dezena} dezenas")
#             elif unidade == 1:
#                 print(f"{num} = {centena} centena, {dezena} dezenas e {unidade} unidade")
#             else:
#                 print(f"{num} = {centena} centena, {dezena} dezenas e {unidade} unidades")
#     else:
#         if dezena == 0:
#             if unidade == 0:
#                 print(f"{num} = {centena} centenas")
#             elif unidade == 1:
#                 print(f"{num} = {centena} centenas e {unidade} unidade")
#             else:
#                 print(f"{num} = {centena} centenas e {unidade} unidades")
#         elif dezena == 1:
#             if unidade == 0:
#                 print(f"{num} = {centena} centenas e {dezena} dezena")
#             elif unidade == 1:
#                 print(f"{num} = {centena} centenas, {dezena} dezena e {unidade} unidade")
#             else:
#                 print(f"{num} = {centena} centenas, {dezena} dezena e {unidade} unidades")
#         else:
#             if unidade == 0:
#                 print(f"{num} = {centena} centenas e {dezena} dezenas")
#             elif unidade == 1:
#                 print(f"{num} = {centena} centenas, {dezena} dezenas e {unidade} unidade")
#             else:
#                 print(f"{num} = {centena} centenas, {dezena} dezenas e {unidade} unidades")
#     return 0
#
# numero = int(input("Digite um número inteiro menor que 1000: "))
# num = numero
# imprima(numero)

# 20-Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
# por aluno e apresentar:
#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10.

# lista_notas = []
# for i in range(3):
#     nota = float(input(f"Digite a nota {i+1}: "))
#     lista_notas.append(nota)
# media = round(sum(lista_notas) / len(lista_notas),1)
# if media == 10:
#     print(f"Aprovado com Distinção, média = {media}.")
# elif media < 10 and media >= 7:
#     print(f"Aprovado, média {media}.")
# elif media < 7 and media >= 0:
#     print(f"Reprovado, média {media}.")
# else:
#     print(f"Média fora do padrão estabelecido, média {media}.")

# 21-Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque  e depois
# informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de
# notas existentes na máquina.
#     Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
#     uma nota de 5 e uma nota de 1;
#     Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
#     quatro notas de 10, uma nota de 5 e quatro notas de 1.

# saque = int(input("Informe o valor que deseja sacar.\nLembrando que, o valor mínino é 10 e o máximo é 600 reais: "))
# valor = saque
# if saque >= 10 and saque <= 600:
#     nota_100 = int(saque / 100)
#     saque = saque % 100
#     notas_50 = int(saque / 50)
#     saque = saque % 50
#     notas_10 = int(saque / 10)
#     saque = saque % 10
#     notas_5 = int(saque / 5)
#     saque = saque % 5
#     notas_1 = saque
#
#     if nota_100 == 0:
#         if notas_50 == 0:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#         elif notas_50 == 1:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50 e {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} nota de 50, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#         else:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50 e {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {notas_50} notas de 50, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#     elif nota_100 == 1:
#         if notas_50 == 0:
#             if notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#         elif notas_50 == 1:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100 e {notas_50} nota de 50.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50 e {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} nota de 50, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#         else:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100 e {notas_50} notas de 50.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50 e {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} nota de 100, {notas_50} notas de 50, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#     else:
#         if notas_50 == 0:
#             if notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} notas de 100.")
#                     elif notas_1 == 1:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} notas de 100 e {notas_1} nota de 1.")
#                     else:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} notas de 100 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(f"Para sacar {valor} reais, será liberado {nota_100} notas de 100 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#         elif notas_50 == 1:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100 e {notas_50} nota de 50.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50 e {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} nota de 50, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#         else:
#             if notas_10 == 1:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50 e {notas_10} nota de 10.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} nota de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} nota de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} nota de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} nota de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} nota de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
#             elif notas_10 == 0:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100 e {notas_50} notas de 50.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_5} nota de 5 e {notas_1} notas de 1.")
#             else:
#                 if notas_5 == 0:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50 e {notas_10} notas de 10.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10 e {notas_1} notas de 1.")
#                 else:
#                     if notas_1 == 0:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10 e {notas_5} nota de 5.")
#                     elif notas_1 == 1:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} nota de 5 e {notas_1} nota de 1.")
#                     else:
#                         print(
#                             f"Para sacar {valor} reais, será liberado {nota_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10 , {notas_5} nota de 5 e {notas_1} notas de 1.")
# else:
#     print(f"O valor de R${saque} não está disponível para saque nesta máquina.")

# 22-Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

# numero = int(input("Digite um número inteiro: "))
# info = numero % 2
# if info == 0:
#     print(f"O número {numero} é par!")
# else:
#     print(f"O número {numero} é impar!")

# 23-Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

# numero = float(input("Digite um número: "))
# num = int(numero)
# if num == numero:
#     print(f"O número {num} é inteiro!")
# else:
#     print(f"O número {numero} é decimal.")

# 24-Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.

# lista_numeros = []
# operacao = ""
# resultado = 0
# for i in range(3):
#     if i == 2:
#         operacao = input("+ => adição, - => subtração, * => multiplicação ou / => divisão"
#                          "\nQual operação deseja realizar? ")
#     else:
#         numero = float(input(f"Digite o número {i+1}: "))
#         lista_numeros.append(numero)
# # Resolvendo a operação
# if operacao == "+":
#     resultado = sum(lista_numeros)
# elif operacao == "-":
#     resultado = lista_numeros[0] - lista_numeros[1]
# elif operacao == "*":
#     resultado = lista_numeros[0] * lista_numeros[1]
# elif operacao == "/":
#     if lista_numeros[1] != 0:
#         resultado = lista_numeros[0] / lista_numeros[1]
#     else:
#         print("\nNão é possível fazer divisão por zero!")
#         exit()
# else:
#     print("\nOperador fora do padrão informado.")
#     exit()
# # Par ou impar / positivo ou negativo / inteiro ou decimal
# if resultado != 0:
#     par_ou_impar = resultado % 2
#     int_ou_dec = int(resultado)
#     if par_ou_impar == 0:
#         if resultado >= 0:
#             if int_ou_dec == resultado:
#                 print(f"\nO resultado {resultado} é um número par, positivo e inteiro.")
#             else:
#                 print(f"\nO resultado {resultado} é um número par, positivo e decimal.")
#         else:
#             if int_ou_dec == resultado:
#                 print(f"\nO resultado {resultado} é um número par, negativo e inteiro.")
#             else:
#                 print(f"\nO resultado {resultado} é um número par, negativo e decimal.")
#     else:
#         if resultado >= 0:
#             if int_ou_dec == resultado:
#                 print(f"\nO resultado {resultado} é um número par, positivo e inteiro.")
#             else:
#                 print(f"\nO resultado {resultado} é um número par, positivo e decimal.")
#         else:
#             if int_ou_dec == resultado:
#                 print(f"\nO resultado {resultado} é um número par, negativo e inteiro.")
#             else:
#                 print(f"\nO resultado {resultado} é um número par, negativo e decimal.")
# else:
#     print("\nO resultado da operação é zero!")

# 25-Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?"
#     O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#     Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#     entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# questionario = {"Telefonou para a vítima?": "", "Esteve no local do crime?": "", "Mora perto da vítima?": "",
#                 "Devia para a vítima?": "", "Já trabalhou com a vítima?": ""}
# positivo = 0
# negativo = 0
# for item in questionario:
#     pergunta = item
#     resposta = input(f"{pergunta} ")
#     questionario[item] = resposta.upper()
# print(questionario)
# for res in questionario.values():
#     if res == "S":
#         positivo += 1
# if positivo <= 1:
#     print("\nClassificação no crime: INOCENTE!")
# elif positivo == 2:
#     print("\nClassificação no crime: SUSPEITA!")
# elif positivo == 3 or positivo == 4:
#     print("\nClassificação no crime: CÚMPLICE!")
# else:
#     print("\nClassificação no crime: ASSASSINA!")

# 26-Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro
#     Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
#     A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#     o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

# litros = float(input("Informe a quantidade de litros desejado: "))
# combustivel = input("Informe o tipo de combustível. Digite A para Álcool ou G para Gasolina: ")
# combustivel = combustivel.upper()
# valor = 0
# if 0 < litros <= 20:
#     if combustivel == "A":
#         valor = (litros * 1.9) - ((litros * 1.9) * 0.03)
#         print(f"\nO valor a ser pago por {litros} litros de álcool, com 3% de desconto, será R${round(valor,2)}.")
#     elif combustivel == "G":
#         valor = (litros * 2.5) - ((litros * 2.5) * 0.04)
#         print(f"\nO valor a ser pago por {litros} litros de gasolina, com 4% de desconto, será R${round(valor,2)}.")
#     else:
#         print("\nCombustível fora do padrão.")
# elif litros > 20:
#     if combustivel == "A":
#         valor = (litros * 1.9) - ((litros * 1.9) * 0.05)
#         print(f"\nO valor a ser pago por {litros} litros de álcool, com 5% de desconto, será R${round(valor,2)}.")
#     elif combustivel == "G":
#         valor = (litros * 2.5) - ((litros * 2.5) * 0.06)
#         print(f"\nO valor a ser pago por {litros} litros de gasolina, com 6% de desconto, será R${round(valor,2)}.")
# else:
#     print("\nValores negativo para litros não será aceito.")

# 27-Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#     receberá ainda um desconto de 10% sobre este total.
#     Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
#     e escreva o valor a ser pago pelo cliente.

# frutaria = {"Morango": "", "Maçã": ""}
# valor_mo = 0
# valor_ma = 0
# kilos_mo = 0
# kilos_ma = 0
# valor_final = 0
# for fruta in frutaria:
#     kilos = float(input(f"Quantos kilos de {fruta}? "))
#     frutaria[fruta] = kilos
# for fruta in frutaria:
#     kilos = frutaria[fruta]
#     if fruta == "Morango":
#         if 0 < kilos <= 5:
#             valor_mo = kilos * 2.5
#             kilos_mo = kilos
#         else:
#             valor_mo = kilos * 2.2
#             kilos_mo = kilos
#     else:
#         if 0 < kilos <= 5:
#             valor_ma = kilos * 1.8
#             kilos_ma = kilos
#         else:
#             valor_ma = kilos * 1.5
#             kilos_ma = kilos
# valor_total = valor_mo + valor_ma
# kilos_total = kilos_mo + kilos_ma
# if valor_total > 25 or kilos_total > 8:
#     valor_final = valor_total - (valor_total * 0.1)
#     print(f"\nValor a ser pago a frutaria R${round(valor_final,2)}.")
# else:
#     print(f"\nValor a ser pago a frutaria R${round(valor_total, 2)}.")

# 28-O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#     porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara
#     o cliente receberá ainda um desconto de 5% sobre o total da compra.
#     Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#     contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
#     valor do desconto e valor a pagar.

acougue = {1: ["File Duplo", 4.9, 5.8], 2: ["Alcatra", 5.9, 6.8], 3: ["Picanha", 6.9, 7.8]}
forma_pagamento = {1: "Dinheiro", 2: "Cartão Crédito", 3: "Cartão Tabajara"}
for carne in acougue:
    print(f"{carne} - {acougue[carne][0]}")
tipo_carne = int(input("Digite o número correspondente para escolher o tipo de carne: "))
kilos = float(input("Digite a quantidade de kilos desejada: "))
print(forma_pagamento)
pagamento = int(input("Digite o número correspondente para escolher a forma de pagamento.\n"
                      "Atenção! Pagamento com Cartão Tabajara tem 5% de desconto: "))
valor = 0
valor_final = 0
desconto = 0
if 0 < kilos <= 5:
    valor = kilos * acougue[tipo_carne][1]
else:
    valor = kilos * acougue[tipo_carne][2]

if pagamento == 3:
    valor_final = valor - (valor * 0.05)
    desconto = valor - valor_final
else:
    valor_final = valor
print(f"\n{datetime.date.today()}\n"
      f"Cupom Fiscal\n"
      f"Tipo de carne: {acougue[tipo_carne][0]}\n"
      f"Quantidade de kg: {kilos}\n"
      f"Preço total: R$ {round(valor,2)}\n"
      f"Forma de pagamento: {forma_pagamento[pagamento]}\n"
      f"Valor do desconto: R$ {round(desconto,2)}\n"
      f"Valor a pagar: R$ {round(valor_final,2)}")