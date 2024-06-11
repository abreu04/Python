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

# numero = int(input("Digite um número inteiro: "))
# num = numero
# lista_primos = []
# divisoes = 0
# while num > 1:
#     i = 2
#     primo = 0
#     while i < num:
#         resto = num % i
#         if resto == 0:
#             primo += 1
#         i += 1
#         divisoes += 1
#     if primo == 0:
#         lista_primos.append(num)
#     num -= 1
# print(f"Número(s) primo(s) entre 1 e {numero}\n{sorted(lista_primos)}\n"
#       f"Foram executadas {divisoes} divisões")

# 24-Faça um programa que calcule o mostre a média aritmética de N notas.

# sentinela = "S"
# notas = []
# while sentinela == "S":
#     n = float(input("Digite uma nota: "))
#     notas.append(n)
#     sentinela = input("Para inserir mais uma nota digite S, ou pressione enter para calcular a média: ")
#     sentinela = sentinela.upper()
# if len(notas) > 0:
#     media = sum(notas) / len(notas)
#     print(f"A média aritmética da(s) nota(s) digitadas é {media}")

# 25-Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
# se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

# sentinela = "S"
# idades = []
# while sentinela == "S":
#     id = float(input("Digite uma idade: "))
#     idades.append(id)
#     sentinela = input("Para inserir mais uma idade digite S, ou pressione enter para calcular a média: ")
#     sentinela = sentinela.upper()
# if len(idades) > 0:
#     media = round(sum(idades) / len(idades))
# if 0 < media <= 25:
#     print(f"A média de idade da turma é {media}, trata-se de uma turma jovem.")
# elif 25 < media <= 60:
#     print(f"A média de idade da turma é {media}, trata-se de uma turma adulta.")
# elif media > 60:
#     print(f"A média de idade da turma é {media}, trata-se de uma turma idosa.")
# else:
#     print(f"A média de idade da turma está fora do padrão esperado, média = {media}.")

# 26-Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# total_eleitores = int (input("Informe um número total de eleitores: "))
# candidatos = {1:["Candidato 1", 0], 2: ["Candidato 2", 0], 3: ["Candidato 3", 0]}
# voto_em_branco = 0
# i = 1
# while i <= total_eleitores:
#     a = 0
#     for a in candidatos:
#         print(candidatos[a][0], end="  ")
#     voto = int(input("\nDigite o número correspondente ao candidato desejado: "))
#     if voto == 1 or voto == 2 or voto == 3:
#         candidatos[voto][1] += 1
#     else:
#         # print("Nenhum dos três!")
#         voto_em_branco += 1
#     i += 1
# print(f"Tivemos {total_eleitores} eleitores nesta eleição.\n"
#       f"A distribuição dos votos ficou da seguinte forma:\n"
#       f"{candidatos[1][0]} recebeu {candidatos[1][1]} voto(s)\n"
#       f"{candidatos[2][0]} recebeu {candidatos[2][1]} voto(s)\n"
#       f"{candidatos[3][0]} recebeu {candidatos[3][1]} voto(s)\n"
#       f"Voto em branco = {voto_em_branco}")

# 27-Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas
# e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

# numero_turmas = 0
# while numero_turmas <= 0:
#     numero_turmas = int(input("Informe a quantidade de turmas: "))
# turmas = {}
# i = 1
# while i <= numero_turmas:
#     alunos = int(input(f"Informe o número de alunos da turma {i}: "))
#     if 0 < alunos <= 40:
#         turmas[i] = alunos
#         i += 1
# print(turmas)
# media = sum(turmas.values()) / len(turmas)
# print(f"A média de alunos por turma é {round(media)}")

# 28-Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

# numero_cds = int(input("Informe a quantidade de CDs da coleção: "))
# colecao = {}
# i = 1
# while i <= numero_cds:
#     cd = int(input(f"Informe o valor no CD {i}: "))
#     colecao[i] = cd
#     i += 1
# media = sum(colecao.values()) / len(colecao)
# print(f"Cada CD custou em média R${round(media,2)}\n"
#       f"A coleção completa, com {len(colecao)} CDs, custou R${round(sum(colecao.values()),2)}")

# 29-O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém
# o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa
# apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
# Você foi contratado para desenvolver o programa que monta esta tabela de preços,
# que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#     Lojas Quase Dois - Tabela de preços
#     1 - R$ 1.99
#     2 - R$ 3.98
#     ...
#     50 - R$ 99.50

# produto = 50
# preco = 1.99
# i = 1
# while i <= produto:
#     print(f"{i} - R$ {i * preco:.2f}")
#     i += 1

# 30-O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta
# a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,
# conforme o exemplo abaixo:
#     Preço do pão: R$ 0.18
#     Panificadora Pão de Ontem - Tabela de preços
#     1 - R$ 0.18
#     2 - R$ 0.36
#     ...
#     50 - R$ 9.00

# paes = 50
# preco = float(input("Informe o valor do pão: "))
# if preco <= 0:
#     print("Olha o prejuízo Sr Manoel!\n"
#           "Vamos gerar essa tabelinha novamente.")
#     exit()
# i = 1
# while i <= paes:
#     print(f"{i} - R$ {i * preco:.2f}")
#     i += 1

# 31-O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências
# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar
# o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar
# o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
# A saída deve ser conforme o exemplo abaixo:
#     Lojas Tabajara
#     Produto 1: R$ 2.20
#     Produto 2: R$ 5.80
#     Produto 3: R$ 0
#     Total: R$ 9.00
#     Dinheiro: R$ 20.00
#     Troco: R$ 11.00
#     ...

# sentinela = " "
# while sentinela != "X":
#     produtos = {}
#     dinheiro = 0
#     troco = 0
#     i = 1
#     while i != 0:
#         preco = float(input(f"Informe o valor do produto {i}: "))
#         produtos[i] = preco
#         i = int(input("Digite o código do próximo produto: "))
#     total = sum(produtos.values())
#     print(f"Lojas Tabajara")
#     a = 1
#     while a <= len(produtos):
#         print(f"Produto {a}: R$ {produtos[a]:.2f}")
#         a += 1
#     print(f"Total: R$ {total:.2f}")
#     dinheiro = float(input("Dinheiro: R$ "))
#     print(f"Troco: R$ {dinheiro-total:.2f}")
#     sentinela = input("\n\nPróxima compra! ")
#     sentinela = sentinela.upper()

# 32-Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
#     Fatorial de: 5
#     5! =  5 . 4 . 3 . 2 . 1 = 120

# numero = int(input("Digite um número inteiro: "))
# prox = numero
# print(f"Fatorial de: {numero}")
# print(f"{numero}! = {numero}", end="")
# while numero > 1:
#     print(f" * {numero - 1}", end="")
#     prox = prox * (numero - 1)
#     numero -= 1
# print(f" = {prox}")

# 33-O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia
# um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
# bem como a média das temperaturas.

# sentinela = ""
# temperaturas = []
# while sentinela != "X":
#     temp = float(input("Informe uma temperatura: "))
#     temperaturas.append(temp)
#     sentinela = input("Pressione enter para digitar mais uma temperatura, ou X para apresentar os resultados: ")
#     sentinela = sentinela.upper()
# print(f"\nInformações sobre as temperaturas digitadas!\n"
#       f"Menor = {min(temperaturas)}\n"
#       f"Maior = {max(temperaturas)}\n"
#       f"Média = {sum(temperaturas) / len(temperaturas)}")

# 34-Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# numero = int(input("Digite um número inteiro: "))
# i = 1
# primo = 0
# while i <= numero:
#     resto = numero % i
#     if resto == 0:
#         primo += 1
#     i += 1
# if primo == 2:
#     print(f"{numero} é primo.")
# else:
#     print(f"{numero} não é primo.")

# 35-Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.

# numero = int(input("Digite um número inteiro: "))
# num = numero
# lista_primos = []
# while numero > 1:
#     a = numero
#     i = 1
#     primo = 0
#     while i <= numero:
#         resto = numero % i
#         if resto == 0:
#             primo += 1
#         i += 1
#     if primo == 2:
#         lista_primos.append(a)
#     numero -= 1
# print(f"Lista de números primos entre 1 e {num}\n"
#       f"{(sorted(lista_primos))}")

# 36-Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final
# devem ser informados também pelo usuário, conforme exemplo abaixo:
#     Montar a tabuada de: 5
#     Começar por: 4
#     Terminar em: 7
#     Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#     5 X 4 = 20
#     5 X 5 = 25
#     5 X 6 = 30
#     5 X 7 = 35
#     Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

# tabuada = int(input("Montar tabuada de: "))
# if tabuada != 0:
#     inicio = int(input("Começar por: "))
#     fim = int(input("Terminar em: "))
#
#     if inicio <= fim:
#         print(f"Vou montar a tabuada de {tabuada}, começando em {inicio} e terminando em {fim}:")
#         while inicio <= fim:
#             print(f"{tabuada} X {inicio} = {tabuada * inicio}")
#             inicio += 1
#     else:
#         print("O número final deve ser maior que o inicial.")
# else:
#     print("Todo número multiplicado por zero é zero!")

# 37-Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
# a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia
# seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
# no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

# Programa sem os códigos dos clientes
# clientes = {}
# codigo = ""
# while codigo != 0:
#     info = []
#     codigo = int(input("Informe o código do cliente: "))
#     if codigo != 0:
#         altura = float(input(f"Informe a altura do cliente {codigo}: "))
#         info.append(altura)
#         peso = float(input(f"Informe o peso do cliente {codigo}: "))
#         info.append(peso)
#         clientes[codigo] = info
# print(clientes)
# alturas = []
# pesos = []
# for i in clientes.values():
#     alturas.append(i[0])
#     pesos.append(i[1])
#     print(i)
# print(f"Maior altura: {max(alturas)}    Menor altura: {min(alturas)}")
# print(f"Maior peso: {max(pesos)}    Menor peso: {min(pesos)}")
# print(f"Média das alturas: {sum(alturas) / len(alturas)}")
# print(f"Média dos pesos: {sum(pesos) / len(pesos)}")

# # Programa com códigos dos clientes
# clientes = {}
# codigo = ""
# while codigo != 0:
#     info = []
#     codigo = int(input("Informe o código do cliente: "))
#     if codigo != 0:
#         altura = float(input(f"Informe a altura do cliente {codigo}: "))
#         info.append(altura)
#         peso = float(input(f"Informe o peso do cliente {codigo}: "))
#         info.append(peso)
#         imc = round(peso / (altura * altura),1)
#         info.append(imc)
#         clientes[codigo] = info
# x = 0
# mais_alto = 0
# mais_baixo = 0
# mais_gordo = 0
# mais_magro = 0
# alto = 1
# baixo = 1
# gordo = 1
# magro = 1
# alturas = []
# pesos = []
# for i in clientes:
#     if x == 0:
#         mais_alto = clientes[i][0]
#         mais_baixo = clientes[i][0]
#         mais_gordo = clientes[i][2]
#         mais_magro = clientes[i][2]
#     x += 1
#     if mais_alto < clientes[i][0]:
#         mais_alto = clientes[i][0]
#         alto = i
#     if mais_baixo > clientes[i][0]:
#         mais_baixo = clientes[i][0]
#         baixo = i
#     if mais_gordo < clientes[i][2]:
#         mais_magro = clientes[i][2]
#         gordo = i
#     if mais_magro > clientes[i][2]:
#         mais_magro = clientes[i][2]
#         magro = i
#     alturas.append(clientes[i][0])
#     pesos.append(clientes[i][1])
# print(f"Cliente mais alto:  Código: {alto} - Altura: {clientes[alto][0]} - Peso: {clientes[alto][1]} - ICM: {clientes[alto][2]}")
# print(f"Cliente mais baixo: Código: {baixo} - Altura: {clientes[baixo][0]} - Peso: {clientes[baixo][1]} - ICM: {clientes[baixo][2]}")
# print(f"Cliente mais gordo: Código: {gordo} - Altura: {clientes[gordo][0]} - Peso: {clientes[gordo][1]} - ICM: {clientes[gordo][2]}")
# print(f"Cliente mais magro: Código: {magro} - Altura: {clientes[magro][0]} - Peso: {clientes[magro][1]} - ICM: {clientes[magro][2]}")
# print(f"Média das altura(s) = {sum(alturas) / len(alturas):.2f}\n"
#       f"Peso médio = {round(sum(pesos) / len(pesos),1)}")

# 38-Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#     a - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#     b - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#     c - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#     Faça um programa que determine o salário atual desse funcionário.
#     Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

# # salario_inicial = 1000
# salario_inicial = float(input("Informe o salário inicial: "))
# salario_atual = salario_inicial
# aumento = 0.015
# i = 1996
# while i <= 2024:
#     salario_atual = salario_atual + (salario_atual * aumento)
#     if salario_atual > 1000000000000:
#         salario = salario_atual / 1000000000000
#         print(f"{i}  {aumento}  {salario:.2f} trillão")
#     elif salario_atual > 1000000000:
#         salario = salario_atual / 1000000000
#         print(f"{i}  {aumento}  {salario:.2f} billão")
#     elif salario_atual > 1000000:
#         salario = salario_atual / 1000000
#         print(f"{i}  {aumento}  {salario:.2f} millão")
#     elif salario_atual > 1000:
#         salario = salario_atual / 1000
#         print(f"{i}  {aumento}  {salario:.2f} mil")
#     else:
#         print(f"{i}  {aumento}  {salario_atual:.2f}")
#     aumento = aumento * 2
#     i += 1

# 39-Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno
# e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

# alunos = {}
# codigo = 0
# while len(alunos) < 2:
#     codigo = int(input(f"Caso o código já exista, a altura será alterada.\n"
#                        f"Digite o código do aluno: "))
#     altura = int(input(f"Digite a altura do aluno: "))
#     alunos[codigo] = altura
# maior = alunos[codigo]
# menor = alunos[codigo]
# ma = 0
# me = 0
# for x in alunos:
#     if maior <= alunos[x]:
#         maior = alunos[x]
#         ma = x
#     if menor >= alunos[x]:
#         menor = alunos[x]
#         me = x
# print(alunos)
# print(f"Maior aluno = código: {ma}  altura: {alunos[ma]}\n"
#       f"Menor aluno = código: {me}  altura: {alunos[me]}")

# 40-Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:
#     Código da cidade;
#     Número de veículos de passeio (em 1999);
#     Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#     Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#     Qual a média de veículos nas cinco cidades juntas;
#     Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

# info = {}
# while len(info) < 3:
#     mais_info = []
#     codigo_cidade = int(input("Informe o código da cidade: "))
#     numero_veiculos = int(input("Informe o número de veículos: "))
#     mais_info.append(numero_veiculos)
#     numero_acidades = int(input("Informe o número de acidentes: "))
#     mais_info.append(numero_acidades)
#     indice_acidentes = round((numero_acidades / numero_veiculos) * 100,1)
#     mais_info.append(indice_acidentes)
#     info[codigo_cidade] = mais_info
#
# print(info)
# maior = 0
# menor = 0
# ma = 0
# me = 0
# x = 1
# veiculos = []
# acidentes = []
# for i in info:
#     if x == 1:
#         maior = info[i][2]
#         menor = info[i][2]
#         ma = i
#         me = i
#     x += 1
#     if maior < info[i][2]:
#         maior = info[i][2]
#         ma = i
#     if menor > info[i][2]:
#         menor = info[i][2]
#         me = i
#     if info[i][0] < 2000:
#         acidentes.append(info[i][1])
#     veiculos.append(info[i][0])
#
# print(f"\nMaior índice de acidentes: {info[ma][2]}, pertence a cidade: {ma}")
# print(f"Menor índice de acidentes: {info[me][2]}, pertence a cidade: {me}")
# print(f"A média de veículos, nas cinco cidades, é igual a {sum(veiculos) / len(veiculos):.1f}")
# print(f"A média de acidentes, nas cidades com menos de 2000 veículos, é igual a {sum(acidentes) / len(acidentes):.1f}")

# 41-Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#     Os juros e a quantidade de parcelas seguem a tabela abaixo:
#     Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#     1       0
#     3       10
#     6       15
#     9       20
#     12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

# valor_divida = 1000
# numero_parcelas = 1
# valor_juros = 0
# valor_parcela = 0
#
# while numero_parcelas <= 12:
#     if numero_parcelas == 1:
#         valor_juros = valor_divida * 0
#     elif numero_parcelas == 3:
#         valor_juros = valor_divida * 0.1
#     elif numero_parcelas == 6:
#         valor_juros = valor_divida * 0.15
#     elif numero_parcelas == 9:
#         valor_juros = valor_divida * 0.2
#     else:
#         valor_juros = valor_divida * 0.25
#
#     if numero_parcelas == 1:
#         valor_parcela = (valor_divida + valor_juros) / numero_parcelas
#         print(f"Valor da Dívida   Valor dos Juros   Quantidade de Parcelas   Valor da Parcela\n"
#               f"R$ {valor_divida:.2f} {valor_juros:>11.2f} {numero_parcelas:>14} {valor_parcela:>30.2f}")
#         numero_parcelas += 2
#     else:
#         valor_parcela = (valor_divida + valor_juros) / numero_parcelas
#         if 1 < numero_parcelas < 12:
#             print(
#                 f"R$ {valor_divida + valor_juros:.2f} {valor_juros:>13.2f} {numero_parcelas:>12} {valor_parcela:>29.2f}")
#             numero_parcelas += 3
#         else:
#             print(
#                 f"R$ {valor_divida + valor_juros:.2f} {valor_juros:>13.2f} {numero_parcelas:>13} {valor_parcela:>28.2f}")
#             numero_parcelas += 3

# 42-Faça um programa que leia uma quantidade indeterminada de números positivos e conte
# quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.

# lista_numeros = []
# numero = 0
# print("\nDigite um número negativo para encerrar a digitação!")
# while numero >= 0:
#     numero = float(input("Digite um número positivo: "))
#     if numero >= 0:
#         lista_numeros.append(numero)
# print(lista_numeros)
# intervalo1 = 0
# intervalo2 = 0
# intervalo3 = 0
# intervalo4 = 0
# fora_intervalo = 0
# for i in lista_numeros:
#     if 0 <= i <=25:
#         intervalo1 += 1
#     elif 26 <= i <= 50:
#         intervalo2 += 1
#     elif 51 <= i <= 75:
#         intervalo3 += 1
#     elif 76 <= i <= 100:
#         intervalo4 += 1
#     else:
#         fora_intervalo += 1
# print(f"Intervalos{"":>19}Qantidades de números\n"
#       f"0-25 {intervalo1:>26}\n"
#       f"26-50 {intervalo2:>25}\n"
#       f"51-75 {intervalo3:>25}\n"
#       f"76-100 {intervalo4:>24}\n"
#       f"Fora dos intervalaos {fora_intervalo:>10}")

# 43-O cardápio de uma lanchonete é o seguinte:
#     Especificação   Código  Preço
#     Cachorro Quente 100     R$ 1,20
#     Bauru Simples   101     R$ 1,30
#     Bauru com ovo   102     R$ 1,50
#     Hambúrguer      103     R$ 1,20
#     Cheeseburguer   104     R$ 1,30
#     Refrigerante    105     R$ 1,00
#     Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
#     Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
#     Considere que o cliente deve informar quando o pedido deve ser encerrado.

# lanchonete = {100: ["Cachorro Quente", 1.20], 101: ["Bauru Simples", 1.30], 102: ["Bauru com ovo", 1.50],
#               103: ["Hambúrguer", 1.20], 104: ["Cheeseburguer", 1.30], 105: ["Refrigerante", 1.00]}
# print(f"Especificação{"":>5}Código{"":>5}Preço")
# for i in lanchonete:
#     a = 20 - len(lanchonete[i][0])
#     print(f"{lanchonete[i][0]} {i:>{a}} {lanchonete[i][1]:>11.2f}")
# print(f"\nDigite 0 para encerrar o pedido!")
# pedido = {}
# codigo = ""
# while codigo != 0:
#     codigo = int(input("Digite o código do produto: "))
#     if codigo != 0:
#         quantidade = int(input(f"Digite a quantidade do produto {codigo}: "))
#         pedido[codigo] = quantidade
# print("\n")
# total = 0
# for i in pedido:
#     for n in lanchonete:
#         if i == n:
#             a = 17 - len(lanchonete[n][0])
#             valor = pedido[i] * lanchonete[n][1]
#             print(f"{lanchonete[n][0]} {pedido[i]:>{a}} x {lanchonete[n][1]:.2f} {valor:>5.2f}")
#             total = total + valor
# print(f"Total do Pedido  R$ {total:.2f}")

# 44-Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
# Os códigos utilizados são: 1 , 2, 3, 4  - Votos para os respectivos candidatos
#     (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#     5 - Voto Nulo
#     6 - Voto em Branco
#     Faça um programa que calcule e mostre:
#     O total de votos para cada candidato;
#     O total de votos nulos;
#     O total de votos em branco;
#     A percentagem de votos nulos sobre o total de votos;
#     A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

# eleicao = {1: ["José", 0], 2: ["João", 0], 3: ["Maria", 0], 4: ["Antônia", 0], 5: ["Nulo", 0], 6: ["Em Branco", 0]}
# voto = ""
# total = 0
# while voto != 0:
#     for i in eleicao:
#         print(f"{i} - {eleicao[i][0]}")
#     voto = int(input("Digite o número correspondente a opção desejada: "))
#     if voto != 0:
#         if 0 < voto <= 6:
#             eleicao[voto][1] += 1
#             total += 1
#         else:
#             print("Opção inexistente!")
# for i in eleicao:
#     a = 15 - len(eleicao[i][0])
#     print(f"{eleicao[i][0]} {eleicao[i][1]:>{a}} votos")
# print(f"Os votos nulos correspondem a {(eleicao[5][1] / total) * 100:.1f}% dos votos válidos.")
# print(f"Os votos em branco correspondem a {(eleicao[6][1] / total) * 100:.1f}% dos votos válidos.")

# 45-Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova
# e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:
#     a - Maior e Menor Acerto;
#     b - Total de Alunos que utilizaram o sistema;
#     c - A Média das Notas da Turma.
#     Gabarito da Prova:
#     01 - A
#     02 - B
#     03 - C
#     04 - D
#     05 - E
#     06 - E
#     07 - D
#     08 - C
#     09 - B
#     10 - A
#     Após concluir isto você poderia incrementar o programa
#     permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

# gabarito = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "E", 7: "D", 8: "C", 9: "B", 10: "A"}
# alunos = {}
# codigo = " "
# while codigo != "0":
#     print("\nPara encerrar a digitação digite 0!")
#     codigo = input("Aluno, para responder a avaliação, informe seu código: ")
#     if codigo != "0":
#         respostas = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: ""}
#         p = 1
#         print(f"Boa sorte, {codigo}!")
#         while p <= len(respostas):
#             resposta = input(f"Digite a resposta da questão {p}: ")
#             resposta = resposta.upper()
#             if resposta == "A" or resposta == "B" or resposta == "C" or resposta == "D" or resposta == "E":
#                 respostas[p] = resposta
#                 p += 1
#             else:
#                 print("Opção inválida!")
#         nota = 0
#         i = 1
#         while i <= 10:
#             if respostas[i] == gabarito[i]:
#                 nota += 1
#             i += 1
#         respostas["Nota"] = nota
#         alunos[codigo] = respostas
# maior = 0
# menor = len(gabarito)
# codigo_maior = []
# codigo_menor = []
# notas = []
# for i in alunos:
#     notas.append(alunos[i]["Nota"])
#     for a in alunos[i]:
#         print(i, a, alunos[i][a])
#     if maior <= alunos[i]["Nota"]:
#         if maior == alunos[i]["Nota"]:
#             codigo_maior.append(i)
#         else:
#             codigo_maior = []
#             codigo_maior.append(i)
#         maior = alunos[i]["Nota"]
#     if menor >= alunos[i]["Nota"]:
#         if menor == alunos[i]["Nota"]:
#             codigo_menor.append(i)
#         else:
#             codigo_menor = []
#             codigo_menor.append(i)
#         menor = alunos[i]["Nota"]
#
#     print("\n")
# print(f"Maior nota = {maior}")
# for i in codigo_maior:
#     print(f"Aluno: {i}")
# print(f"Menor nota = {menor}")
# for i in codigo_menor:
#     print(f"Aluno: {i}")
# print(f"Número de Alunos que responderam a avaliação = {len(notas)}")
# print(f"Média das Notas obtidas = {sum(notas) / len(notas)}")

# # Programa com indicacao de respostas corretas e erradas, e gabarito montado pelo Professor
# print(f"Olá Professor! Vamos montar o Gabarito da Avaliação.")
# lista_alternativas = []
# a = 1
# alternativa = " "
# print("Para encerrar a digitação das ALTERNATIVAS, pressione Enter!")
# while alternativa != "":
#     alternativa = input("Digite uma alternativa de respospa: ").upper()
#     if alternativa not in lista_alternativas and alternativa != "":
#         lista_alternativas.append(alternativa)
#     else:
#         print("Alternativa já existe!")
# print(lista_alternativas)
#
# gabarito = {}
# p = 1
# resposta = " "
# print(f"Professor, agora, informe a alternativa correta de cada questão!")
# print("Para encerrar a digitação das QUESTÕES, pressione Enter!")
# while resposta != "":
#     resposta = input(f"Digite a resposta da questão {p}: ").upper()
#     if resposta != "":
#         if resposta in lista_alternativas:
#             gabarito[p] = resposta
#             p += 1
#         else:
#             print("Esta alternativa não foi definida!")
# print(gabarito)
#
# alunos = {}
# codigo = " "
# notas = []
# while codigo != "0":
#     print("\nAlunos! Para encerrar a digitação digite 0!")
#     codigo = input("Para responder a avaliação, informe seu código: ")
#     if codigo != "0":
#         respostas = {}
#         p = 1
#         nota = 0
#         print(f"Boa sorte, {codigo}!")
#         while p <= len(gabarito):
#             resposta_correcao = []
#             resposta = input(f"Digite a resposta da questão {p}: ").upper()
#             if resposta in lista_alternativas:
#                 if resposta == gabarito[p]:
#                     resposta_correcao.append(resposta)
#                     resposta_correcao.append("Correta")
#                     nota += 1
#                 else:
#                     resposta_correcao.append(resposta)
#                     resposta_correcao.append("Incorreta")
#                 respostas[p] = resposta_correcao
#                 p += 1
#             else:
#                 print("Alternativa inexistente!")
#         respostas["Nota"] = nota
#         alunos[codigo] = respostas
# print("\n")
# maior = 0
# menor = len(gabarito)
# codigo_maior = []
# codigo_menor = []
#
# for i in alunos:
#     notas.append(alunos[i]["Nota"])
#     print(gabarito)
#     for a in alunos[i]:
#         print(i, a, alunos[i][a])
#     if maior <= alunos[i]["Nota"]:
#         if maior == alunos[i]["Nota"]:
#             codigo_maior.append(i)
#         else:
#             codigo_maior = []
#             codigo_maior.append(i)
#         maior = alunos[i]["Nota"]
#     if menor >= alunos[i]["Nota"]:
#         if menor == alunos[i]["Nota"]:
#             codigo_menor.append(i)
#         else:
#             codigo_menor = []
#             codigo_menor.append(i)
#         menor = alunos[i]["Nota"]
#     print("\n")
# print(f"Maior nota = {maior}")
# for i in codigo_maior:
#     print(f"Aluno: {i}")
# print(f"Menor nota = {menor}")
# for i in codigo_menor:
#     print(f"Aluno: {i}")
# print(f"Número de Alunos que responderam a avaliação = {len(notas)}")
# print(f"Média das Notas obtidas = {sum(notas) / len(notas)}")

# 46-Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
# e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto
# e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
# Os saltos são informados na ordem da execução, portanto não são ordenados.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
#
# Resultado final:
# Rodrigo Curvêllo: 5.9 m

# competicao = {}
# atleta = " "
# while atleta != "":
#     atleta = input("Informe o nome do Atleta: ")
#     if atleta != "":
#         lista_saltos = []
#         i = 1
#         while i <= 5:
#             lista_saltos.append(float(input(f"Digite a altura do salto {i}: ")))
#             i += 1
#         competicao[atleta] = lista_saltos
# media = 0
# saltos_final = []
#
# for s in competicao:
#     print(f"Atleta: {s}\n\n"
#           f"Primeiro Salto: {competicao[s][0]} m\n"
#           f"Segundo Salto: {competicao[s][1]} m\n"
#           f"Terceiro Salto: {competicao[s][2]} m\n"
#           f"Quarto Salto: {competicao[s][3]} m\n"
#           f"Quinto Salto: {competicao[s][4]} m\n")
#     saltos_final = competicao[s]
#     saltos_final.sort()
#     print(f"Melhor salto: {saltos_final.pop(-1)} m")
#     print(f"Pior salto: {saltos_final.pop(0)} m")
#     media = sum(saltos_final) / len(saltos_final)
#     print(f"Média dos demais saltos : {media:.1f} m")
#     print(f"Resultado Final:\n"
#           f"{s}: {media:.1f} m\n")

# 47-Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta
# e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
# com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

# competicao_ginastica = {}
# atleta = " "
# while atleta != "":
#     print("\nPressione Enter para encerrar a digitação!")
#     atleta = input("Digite o nome do Atleta: ")
#     if atleta != "":
#         notas = []
#         i = 1
#         while i <= 7:
#             notas.append(float(input(f"Digite a nota {i}: ")))
#             competicao_ginastica[atleta] = notas
#             i += 1
# notas_finais = []
# for i in competicao_ginastica:
#     print(f"Atleta: {i}")
#     notas_finais = competicao_ginastica[i]
#     for n in notas_finais:
#         print(f"Nota: {n}")
#     notas_finais.sort()
#     print(f"Resultado final:\n"
#           f"Atleta: {i}\n"
#           f"Melhor nota: {notas_finais.pop(-1)}\n"
#           f"Pior nota: {notas_finais.pop(0)}\n"
#           f"Média: {sum(notas_finais) / len(notas_finais):.1f}\n")

# 48-Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#     Exemplo:
#       12376489
#       => 98467321

# numero = int(input("Digite um número inteiro positivo: "))
# num = numero
# invertido = 0
# while numero > 0:
#     resto = numero % 10
#     invertido = (invertido * 10) + resto
#     numero = int(numero / 10)
# print(f"Número: {num}\n"
#       f"Número invertido: {invertido}")

# 49-Faça um programa que mostre os n termos da Série a seguir:
#     S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#     Imprima no final a soma da série.

# numero = int(input("Digite um número inteiro positivo: "))
# n = 1
# soma = 0
# print(f"Soma = {n}/{n} ", end="")
# while n <= numero:
#     soma = soma + (n / ((n - 1) + n))
#     n += 1
#     if n <= numero:
#         print(f"+ {n}/{(n-1)+n}", end=" ")
# print(f"+ ... + n/(n-1)+n")
# print(f"Soma = {soma:.1f}")

# 50-Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

numero = 10
n = 1
h = 0
print(f"H = {int(1/n)}", end="")
while n <= numero:
    h = h + 1/n
    n += 1
    if n <= numero:
        print(f" + 1/{n}", end="")
print(f"\nPara N = {numero}, H = {h:.1f}")
