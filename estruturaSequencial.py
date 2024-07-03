# 1-Faça um Programa que mostre a mensagem "Alo mundo" na tela
# print("Alo mundo")

# 2-Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]
# numero_informado = input("Digite um mumero: ")
# print(f"O número informado foi {numero_informado}")

# 3-Faça um Programa que peça dois números e imprima a soma
# num_1 = int(input("Digite o primeiro número: "))
# num_2 = int(input("Digite o segundo número: "))
# soma = num_1 + num_2
# print(f"A soma de {num_1} + {num_2} é igual {soma}")

# 4-Faça um Programa que peça as 4 notas bimestrais e mostre a média
# lista_notas = []
# for i in range(4):
#     nota = float(input(f"Digite a nota {i}: "))
#     lista_notas.append(nota)
# media = sum(lista_notas)/4
# print(f"A média das notas informadas é {media}")

# 5-Faça um Programa que converta metros para centímetros
# comprimento_metro = float(input("Vamos converter metros em centímetros! Digite um número: "))
# comprimento_centimetro = comprimento_metro * 100
# print(f"{comprimento_metro}m corresponde a {comprimento_centimetro}cm.")

# 6-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
# raio = float(input("Vamos calcular a área de um círculo, por favor informe um raio: "))
# pi = 3.14
# area = pi * (raio * raio)
# print(f"A área do círculo é {area}.")

# 7-Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
# base = float(input("Vamos calcular a área de um quadrado. Informe a medida da base ou altura: "))
# area = base * base
# print(f"O dobro da área calculada é {area * 2}")

# 8-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês
# ganho_por_hora = float(input("Informe quanto ganha por hora trabalhada: "))
# horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
# salario = ganho_por_hora * horas_trabalhadas
# print(f"O salário deste mês será de R${salario}")

# 9-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)
# fahrenheit = float(input("Vamos transformar Fahrenheit em Celsius. Informe a temperatura em Fahrenheit: "))
# celsius = 5 * ((fahrenheit - 32) / 9)
# celsius = round(celsius, 1)
# print((f"{fahrenheit}° Fahrenheit equivale a {celsius}° Celsius."))

# 10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
# celsius = float(input("Vamos transformar Celsius em Fahrenheit. Informe a temperatura em Celsius: "))
# fahrenheit = (celsius * (9 / 5)) + 32
# fahrenheit = round(fahrenheit, 1)
# print(f"{celsius}° Celsius equivale a {fahrenheit}° Fahrenheit.")

# 11-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# int_1 = int(input("Digite o primeiro número inteiro: "))
# int_2 = int(input("Digite o segundo número inteiro: "))
# real_1 = float(input("Digite um número real: "))
#
# # 11a- O produto do dobro do primeiro com metade do segundo
# solucao_a = (2 * int_1) * (int_2 / 2)
# print(f"O produto do dobro de {int_1} com metade de {int_2} é igual a {solucao_a}.")
#
# # 11b- A soma do triplo do primeiro com o terceiro
# solucao_b = (3 * int_1) + real_1
# print(f"A soma do triplo de {int_1} com {real_1} é igual a {solucao_b}.")
#
# # 11c- O terceiro elevado ao cubo
# solucao_c = real_1 * real_1 * real_1
# print(f"{real_1} elevado ao cubo é igual a {solucao_c}.")

# 12-Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
# altura = 1.64
# peso_ideal = (72.7 * altura) - 58
# print((f"Seu peso ideal é {round(peso_ideal,1)}kg."))

# 13-Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: para homens: (72.7*h) - 58 e para mulheres: (62.1*h) - 44.7
# altura = float(input("Informe sua altura em centímetros: "))
# altura = altura / 100
# genero = input("Informe seu genero. Digite F para feminino ou M para masculino: ")
# genero = genero.upper()
# if "F" in genero:
#     peso_ideal = (62.1 * altura) - 44.7
#     print(f"Seu peso ideal para uma mulher com altura {round(altura,2)}m é {round(peso_ideal,1)}kg.")
# elif "M" in genero:
#     peso_ideal = (72.7 * altura) - 58
#     print(f"O peso ideal para um homem com altura {round(altura,2)}m é {round(peso_ideal,1)}kg.")
# else:
#     print(f"Informe F ou M no campo de genero!")

# 14-João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas
# peso_pescado = float(input("Informe quantos quilos de peixe foram pescados hoje: "))
# peso_limite = 50
# peso_excedido = peso_pescado - peso_limite
# if peso_excedido > 0:
#     multa_excesso = 4.00 * peso_excedido
#     print(f"O excesso de peixes pescados foi de {peso_excedido}kg, logo a multa será de R${round(multa_excesso,2)}.")
# else:
#     print("Não houve excesso de peixes pescados, portanto não há multa!")

# 15-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# ganho_por_hora = float(input("Informe quanto ganha por hora trabalhada: "))
# horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
# salario_bruto = ganho_por_hora * horas_trabalhadas
# imposto_renda = salario_bruto * 0.11
# inss = salario_bruto * 0.08
# sindicato = salario_bruto * 0.05
# salario_liquido = salario_bruto - imposto_renda - inss - sindicato
#
# # 15a-salário bruto
# print(f"O salário bruto é R${salario_bruto}.")
# # custo com imposto de renda
# print(f"Pagou R${imposto_renda} de Imposto de renda.")
# # 15b-quanto pagou ao INSS
# print(f"Pagou R${inss} ao INSS.")
# # 15c-quanto pagou ao sindicato
# print(f"Pagou R${sindicato} ao Sindicato.")
# # 15d-o salário líquido
# print(f"O salário líquido é R${salario_liquido}.")

# 16-Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total
# area_pintura = float(input("Informe o tamanho da área a ser pintada em m²: "))
# latas_tintas_necessarias = area_pintura / 54
# latas_total = round(latas_tintas_necessarias + 0.5)
# valor = latas_total * 80
# print(f"Será necessário {latas_total} lata(s) de tinta para pintar {area_pintura}m², e o custo será de R${valor}.")

# 17-Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# area_pintura = float(input("Informe o tamanho da área a ser pintada em m²: "))
# area_pintura_com_folga = area_pintura + area_pintura * 0.1
#
# # comprar apenas latas de 18 litros
# latas = area_pintura_com_folga / 108
# if area_pintura_com_folga % 108 > 0:
#     latas = round(latas + 0.5)
# custo_total = latas * 80
# print(f"Para pintar {area_pintura}m² será necessário {latas} lata(s) de tinta de 18 litros.")
# print(f"Custo total para comprar somente latas será de R${custo_total}")
# print("\n")
# # comprar apenas galões de 3,6 litros
# galao = area_pintura_com_folga / 21.6
# if area_pintura_com_folga % 21.6 > 0:
#     galao = round(galao + 0.5)
# custo_total = galao * 25
# print(f"Para pintar {area_pintura}m² será necessário {galao} galão de tinta de 3,6 litros.")
# print(f"Custo total para comprar somente galões será de R${custo_total}")
# print("\n")
# # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
# # sempre arredonde os valores para cima, isto é, considere latas cheias
# litros_tinta = area_pintura_com_folga * (1/6)
# litros = litros_tinta
# latas = 0
# galao = 0
# while litros_tinta > 0:
#     if litros_tinta >= 10.8:
#         latas = litros_tinta / 18
#         latas = round(latas)
#         litros_tinta = litros_tinta - (latas * 18)
#     else:
#         galao = litros_tinta / 3.6
#         galao = round(galao + 0.5)
#         litros_tinta = litros_tinta - (galao * 3.6)
#
# custo_total = (latas * 80) + (galao * 25)
# if latas > 0 and galao > 0:
#     print(f"Para pintar {area_pintura}m² será necessário {round(litros,2)} litros de tinta.")
#     print(f"Você precisará de {latas} latas de 18 litros e {galao} galão de 3.6 litros de tinta.")
#     print(f"O custo total de R${custo_total}.")
# elif latas > 0 and galao <= 0:
#     print(f"Para pintar {area_pintura}m² será necessário {round(litros, 2)} litros de tinta.")
#     print(f"Você precisará de {latas} latas de 18 litros de tinta.")
#     print(f"O custo total de R${custo_total}.")
# elif latas <= 0 and galao > 0:
#     print(f"Para pintar {area_pintura}m² será necessário {round(litros, 2)} litros de tinta.")
#     print(f"Você precisará de {galao} galão de 3.6 litros de tinta.")
#     print(f"O custo total de R${custo_total}.")
# else:
#     print("Se você não pintar nada, o desconto é maior!")

# 18-Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link
# de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
# tamanho_arquivo = float(input("Informe o tamanho (em MB) do arquivo que deseja fazer o download: "))
# velocidade_link = float(input("Informe a velocidade (em Mbps) da internet que será usada: "))
# tempo_download_seg = tamanho_arquivo / (velocidade_link/ 8)
# tempo_download_min = tempo_download_seg / 60
# print(f"O download de {tamanho_arquivo}MB no link de {velocidade_link}Mbps levará aproximadamente {round(tempo_download_min,1)} minutos.")