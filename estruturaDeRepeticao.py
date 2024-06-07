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

info = {}
while len(info) < 3:
    mais_info = []
    codigo_cidade = int(input("Informe o código da cidade: "))
    numero_veiculos = int(input("Informe o número de veículos: "))
    mais_info.append(numero_veiculos)
    numero_acidades = int(input("Informe o número de acidentes: "))
    mais_info.append(numero_acidades)
    info[codigo_cidade] = mais_info
print(info)
