# 1-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

# nota = -1
# while not 0 <= nota <=10:
#     nota = float(input("Digite uma nota entre 0 e 10: "))
# print("Terminamos. Parabéns!")

# 2-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostre uma mensagem de erro e volte a pedir as informações.

# usuario = ""
# senha = ""
# i = 1
# while senha == usuario:
#     if i > 1:
#         print("Erro! Usuário e Senha não devem ser iguais!")
#     usuario = input("Digite seu usuário: ")
#     senha = input("Digite sua senha: ")
#     i += 1

# 3-Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

# valido = 0
# while valido < 5:
#     if valido != 0:
#         print("\nMais ATENÇÃO ao preencher as informações, usuário!")
#     nome = input("O nome deve ter mais que 03 caracteres. Informe o nome: ")
#     valido = 0
#     if len(nome) > 3:
#         valido += 1
#     idade = int(input("Informe a idade, entre 0 e 150: "))
#     if 0 < idade < 150:
#         valido += 1
#     salario = float(input("Salário deve ser maior que zero. Informe o salário: "))
#     if salario > 0:
#         valido += 1
#     sexo = input("Informe o sexo. Digite F ou M: ")
#     sexo = sexo.upper()
#     if sexo == "F" or sexo == "M":
#         valido += 1
#     lista_estado_civil = {"S": "Solteiro", "c": "Casado", "v": "Viúvo", "D": "Divorciado"}
#     print(lista_estado_civil)
#     estado_civil = input("Digite a letra correspondente ao estado civil: ")
#     estado_civil = estado_civil.upper()
#     if estado_civil in lista_estado_civil:
#         valido += 1

# 4-Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
# ou iguale a população do país B, mantidas as taxas de crescimento.

# pais_a = 80000
# pais_b = 200000
# ano = 0
# while pais_a < pais_b:
#     pais_a = pais_a * 1.03
#     pais_b = pais_b * 1.015
#     ano += 1
# if pais_a == pais_b:
#     print(f"Em {ano} anos a população do País A ({round(pais_a,2)}) "
#           f"se igualará a população do País B ({round(pais_b,2)}).")
# else:
#     print(f"Em {ano} anos a população do País A ({round(pais_a,2)}) "
#           f"ultrapassará a população do País B ({round(pais_b,2)}).")

# 5-Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

# sentinela = "S"
# while sentinela == "S":
#     pais_a = float(input("Informe o número de habitantes do Pais A: "))
#     pais_a_tx = float(input("Informe a taxa de crescimento populacional do Pais A: "))
#     pais_b = float(input("Informe o número de habitantes do Pais B: "))
#     pais_b_tx = float(input("Informe a taxa de crescimento populacional do Pais A: "))
#     ano = 0
#     if pais_a > 0 and pais_a_tx > 0 and pais_b > 0 and pais_b_tx > 0:
#         pais_a_tx = (pais_a_tx / 100) + 1
#         pais_b_tx = (pais_b_tx / 100) + 1
#         while pais_a < pais_b:
#             pais_a = pais_a * pais_a_tx
#             pais_b = pais_b * pais_b_tx
#             ano += 1
#         if pais_a == pais_b:
#             print(f"\nEm {ano} anos a população do País A ({round(pais_a,2)}) "
#                   f"se igualará a população do País B ({round(pais_b,2)}).")
# #         else:
#             print(f"\nEm {ano} anos a população do País A ({round(pais_a,2)}) "
#                   f"ultrapassará a população do País B ({round(pais_b,2)}).")
#     else:
#         print("\nTodas entradas devem ser maior que zero para conseguirmos simular "
#               "o crescimento populacional dos país A e B.")
#
#     sentinela = input("\nDigite S para repeir a operação ou qualquer outra letra para encerrar o programa: ")
#     sentinela =  sentinela.upper()

# 6-Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

# numero = 0
# while numero < 20:
#     numero += 1
#     # um ao lado do outro
#     # print(numero, end=" ")
#     # um embaixo do outro
#     print(numero)

# 7-Faça um programa que leia 5 números e informe o maior número.

# lista_numeros = []
# for i in range(5):
#     numero = float(input(f"Digite o número {i+1}: "))
#     lista_numeros.append(numero)
# print(f"O maior número digitado foi {max(lista_numeros)}.")

# 8-Faça um programa que leia 5 números e informe a soma e a média dos números.

# lista_numeros = []
# for i in range(5):
#     numero = float(input(f"Digite o número {i+1}: "))
#     lista_numeros.append(numero)
# print(f"A soma dos números digitados é {sum(lista_numeros)}.\n"
#       f"E a média dos mesmo é {sum(lista_numeros) / len(lista_numeros)}.")

# 9-Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# numero = 1
# while numero < 50:
#     print(numero, end=" ")
#     numero += 2

# 10-Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo compreendido por eles.

# primeiro = int(input("Digite o primeiro número inteiro: "))
# segundo = int(input("Digite o segundo número inteiro: "))
# prox = primeiro + 1
# while prox < segundo:
#     resto = prox % 2
#     if resto == 0:
#         print(prox, end=" ")
#     prox +=1

# 11-Altere o programa anterior para mostrar no final a soma dos números

# primeiro = int(input("Digite o primeiro número inteiro: "))
# segundo = int(input("Digite o segundo número inteiro: "))
# prox = primeiro + 1
# soma = 0
# while prox < segundo:
#     resto = prox % 2
#     if resto == 0:
#         print(prox, end=" ")
#         soma = soma + prox
#     prox +=1
# print(f"\nSoma = {soma}")

# 12-Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#     Tabuada de 5:
#     5 X 1 = 5
#     5 X 2 = 10
#     ...
#     5 X 10 = 50
# Tabuada completa
# sentinela = "S"
# while sentinela == "S":
#     numero = int(input("Digite o número que deseja ver a tabuada: "))
#     operacoes = {1: "+", 2: "-", 3: "x", 4: ":"}
#     print(operacoes)
#     operador = int(input("Digite o número correspondente a operação desejada: "))
#     i = 1
#     n = numero + 1
#     x = numero
#     while i <= 10:
#         if operador == 1:
#             print(f"{numero} {operacoes[operador]} {i} = {numero + i}")
#         elif operador == 2:
#             print(f"{n} {operacoes[operador]} {numero} = {n - numero}")
#             n += 1
#         elif operador == 3:
#             print(f"{numero} {operacoes[operador]} {i} = {numero * i}")
#         elif operador == 4:
#             print(f"{x} {operacoes[operador]} {numero} = {round(x / numero)}")
#             x += numero
#         else:
#             print("operador fora do padrão.")
#             break
#         i += 1
#     sentinela = input("Digite S caso queira operar novamente ou qualquer outra coisa para encerrar: ")
#     sentinela = sentinela.upper()

# 13-Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado
# ao segundo número. Não utilize a função de potência da linguagem.

# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))
# i = 1
# potencia = base
# while i < expoente:
#     potencia = potencia * base
#     i += 1
# print(f"{base} elevado {expoente} é igual {potencia}")

# 14-Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números impares.

# lista_numeros = []
# par = 0
# impar = 0
# for i in range(10):
#     numero = int(input(f"Digite o número {i+1}: "))
#     lista_numeros.append(numero)
# for num in lista_numeros:
#     res = num % 2
#     if res == 0:
#         par += 1
#     else:
#         impar += 1
# print(f"Dentre os números digitados há {par} pares e {impar} impares.")

# 15-A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

# ant = 1
# prox = 1
# res = 0
# n = 10
# i = 0
# while i <= n:
#     if i == 0:
#         print(ant, prox, end=" ")
#     else:
#         print(res, end=" ")
#     res = ant + prox
#     ant = prox
#     prox = res
#     i += 1

# 16-A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

# ant = 1
# prox = 1
# res = 0
# n = 500
# i = 0
# while not i > n:
#     if i == 0:
#         print(ant, prox, end=" ")
#     else:
#         print(res, end=" ")
#     res = ant + prox
#     ant = prox
#     prox = res
#     i = res
# print(res)

# 17-Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# valor = int(input("Vamos calcular o fatorial. Digite um número inteiro: "))
# fat = valor
# i = valor
# print(f"{valor}! = {i}", end="")
# while i != 1:
#     fat = fat * (i - 1)
#     i -= 1
#     print(f" . {i}", end="")
# print(f" = {fat}")

# 18-Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

# quantidade_numero = int(input("Informe quantos números terá no conjunto: "))
# numeros = []
# for i in range(quantidade_numero):
#     numero = float(input(f"Digite o npumero {i+1}: "))
#     numeros.append(numero)
# print(f"Menor = {min(numeros)}   Maior = {max(numeros)}   Soma = {sum(numeros)}")

# 19-Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

# quantidade_numero = int(input("Informe quantos números terá no conjunto: "))
# numeros = []
# i = 1
# while i <= quantidade_numero:
#     numero = float(input(f"Digite o npumero {i}: "))
#     if 0 < numero < 1000:
#         numeros.append(numero)
#         i += 1
# print(f"Menor = {min(numeros)}   Maior = {max(numeros)}   Soma = {sum(numeros)}")

# 20-Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
# e limitando o fatorial a números inteiros positivos e menores que 16.

# sentinela = "S"
# print("Vamos calcular o fatorial!")
# while sentinela == "S":
#     valor = int(input("\nDigite um número inteiro: "))
#     if 0 < valor < 16:
#         fat = valor
#         i = valor
#         print(f"{valor}! = {i}", end="")
#         while i != 1:
#             fat = fat * (i - 1)
#             i -= 1
#             print(f" . {i}", end="")
#         print(f" = {fat}")
#     else:
#         print("\nO cálculo está limitado a números inteiros positivos e menores que 16.")
#     sentinela = input("\nPara calcular o fatorial de um novo número digite S,"
#                       "\nou qualquer outra coisa para sair do programa: ")
#     sentinela = sentinela.upper()

# 21-Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# sentinela = "S"
# while sentinela == "S":
#     numero = int(input("Digite um número inteiro: "))
#     i = 0
#     primo = 0
#     nao_primo = 0
#     while i <= numero:
#         res = numero % (i + 1)
#         if res == 0:
#             primo += 1
#         i += 1
#
#     if primo != 2:
#         print(f"{numero} não é primo")
#     else:
#         print(f"{numero} é primo.")
#     sentinela = input("\nPara verificar um novo número digite S,"
#                       "\nou qualquer outra coisa para sair do programa: ")
#     sentinela = sentinela.upper()

# 22-Altere o programa de cálculo dos números primos, informando,
# caso o número não seja primo, por quais número ele é divisível.

# sentinela = "S"
# while sentinela == "S":
#     numero = int(input("Digite um número inteiro: "))
#     i = 0
#     primo = 0
#     nao_primo = 0
#     divisores = []
#     while i <= numero:
#         res = numero % (i + 1)
#         if res == 0:
#             primo += 1
#             divisores.append((i+1))
#         i += 1
#
#     if primo != 2:
#         print(f"{numero} não é primo")
#         print(divisores)
#     else:
#         print(f"{numero} é primo.")
#     sentinela = input("\nPara verificar um novo número digite S,"
#                       "\nou qualquer outra coisa para sair do programa: ")
#     sentinela = sentinela.upper()

# 23-Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
