# 1-Tamanho de strings.
# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#     Compara duas strings
#     String 1: Brasil Hexa 2006
#     String 2: Brasil! Hexa 2006!
#     Tamanho de "Brasil Hexa 2006": 16 caracteres
#     Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#     As duas strings são de tamanhos diferentes.
#     As duas strings possuem conteúdo diferente.

# str1 = "String 11"
# str2 = "String 2"
# print(f'Tamanho de "{str1}": {len(str1)} caracteres')
# print(f'Tamanho de "{str2}": {len(str2)} caracteres')
# if len(str1) == len(str2):
#     print("As duas strings são de mesmo tamamho.")
# else:
#     print("As duas strings são de tamamhos diferentes.")
#
# if str1 == str2:
#     print("As duas strings possuem o mesmo conteúdo.")
# else:
#     print("As duas strings possuem conteúdo diferente.")

# 2-Nome ao contrário em maiúsculas.
# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre
# o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# nome = input("Digite o nome: ").upper()
# i = len(nome) - 1
# while i >= 0:
#     print(nome[i], end="")
#     i -= 1

# 3-Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#     F
#     U
#     L
#     A
#     N
#     O

# nome = input("Digite o nome: ").upper()
# i = 0
# while i < len(nome):
#     print(nome[i])
#     i += 1

# 4-Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#     F
#     FU
#     FUL
#     FULA
#     FULAN
#     FULANO

# nome = input("Digite o nome: ").upper()
# i = 0
# nome_escada = ""
# while i < len(nome):
#     nome_escada = nome_escada + nome[i]
#     print(nome_escada)
#     i += 1

# 5-Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#     FULANO
#     FULAN
#     FULA
#     FUL
#     FU
#     F

# nome = input("Digite o nome: ").upper()
# i = len(nome) - 1
# nome_escada_invertida = ""
# while i >= 0:
#     a = 0
#     while a <= i:
#         nome_escada_invertida = nome_escada_invertida + nome[a]
#         a += 1
#     print(nome_escada_invertida)
#     nome_escada_invertida = ""
#     i -= 1

# 6-Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário
# e imprima a data com o nome do mês por extenso.
#     Data de Nascimento: 29/10/1973
#     Você nasceu em  29 de Outubro de 1973.

# meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
#              9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
# data_nasc = "04/11/1986"
#
# if len(data_nasc) != 10 and data_nasc[2:3] != "/" and data_nasc[5:6] != "/":
#     print("Data inválida!")
# else:
#     if int(data_nasc[6:]) > 0:
#         print(f"Data de Nascimento: {data_nasc}")
#         print(f"Você nasceu em {data_nasc[:2]} de {meses[int(data_nasc[3:5])]} de {data_nasc[6:]}.")
#     else:
#         print("Data inválida!")

# 7-Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u

# frase = input("Digite uma frase: ")
# dic_vogais = {" ": 0, "a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
# for i in frase.lower():
#     for v in dic_vogais:
#         if i == v:
#             dic_vogais[v] = dic_vogais[v] + 1
# for i in dic_vogais:
#     if i == " ":
#         print(f"Existem {dic_vogais[i]} espaços em branco na frase.")
#     else:
#         print(f'A vogal "{i}" aparece {dic_vogais[i]} vezes.')
#
# # Other version
# frase = input("Digite uma frase: ")
# dic_vogais = {" ": 0, "a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
# for i in dic_vogais:
#     dic_vogais[i] = frase.lower().count(i)
# for i in dic_vogais:
#     if i == " ":
#         print(f"Existem {dic_vogais[i]} espaços em branco na frase.")
#     else:
#         print(f'A vogal "{i}" aparece {dic_vogais[i]} vezes.')

# 8-Palíndromo.
# Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
# ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

# seq_carateres = "Subi no onibus"
# seq_normal = ""
# seq_invertida = ""
# for i in seq_carateres.lower():
#     if i != " " and i != ".":
#         seq_normal = seq_normal + i
# i = len(seq_normal) - 1
# while i >= 0:
#     seq_invertida = seq_invertida + seq_normal[i]
#     i -= 1
# if seq_normal == seq_invertida:
#     print(f'"{seq_carateres}" é palídromo.')
# else:
#     print(f'"{seq_carateres}" não é palídromo.')

# 9-Verificação de CPF.
# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique
# se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

# cpf = input("Digite o CPF, no formato xxx.xxx.xxx-xx: ")
# if cpf[3:4] == "." and cpf[7:8] == "." and cpf[11:12] == "-" and len(cpf) == 14:
#     # print("Formato correto")
#     so_numeros = ""
#     for i in cpf:
#         if i != "." and i != "-":
#             so_numeros = so_numeros + i
#     # print(so_numeros)
#     i = 8
#     x = 2
#     verificador = 0
#     while i >= 0:
#         verificador = verificador + (int(so_numeros[i]) * x)
#         i -= 1
#         x += 1
#     # print(verificador)
#     dezena = verificador % 11
#     if dezena == 0 or dezena == 1:
#         dezena = 0
#     else:
#         dezena = 11 - dezena
#     # print(dezena)
#
#     if dezena == int(so_numeros[9]):
#         i = 9
#         x = 2
#         verificador = 0
#         while i >= 0:
#             verificador = verificador + (int(so_numeros[i]) * x)
#             i -= 1
#             x += 1
#         # print(verificador)
#         unidade = verificador % 11
#         if unidade == 0 or unidade == 1:
#             unidade = 0
#         else:
#             unidade = 11 - unidade
#         # print(unidade)
#         if unidade == int(so_numeros[10]):
#             print(f"O CPF {cpf} é válido.")
#         else:
#             print(f"O CPF {cpf} é inválido.")
#     else:
#         print(f"O CPF {cpf} é inválido.")
# else:
#     print("Formato inválido")

# 10-Número por extenso.
# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso

# dic_numeros = {1: {1: "um", 10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze",
#                    16: "dezesseis", 17: "dezesete", 18: "dezoito", 19: "dezenove"},
#                2: ["dois", "vinte"], 3: ["três", "trinta"], 4: ["quatro", "quarenta"], 5: ["cinco", "cinquenta"],
#                6: ["seis", "sessenta"], 7: ["sete", "setenta"], 8: ["oito", "oitenta"], 9: ["nove", "noventa"]}
# numero = int(input("Digite um número entre 1 e 99: "))
# if numero > 9:
#     unidade = numero % 10
#     dezena = int(numero / 10)
#     # print(dezena, unidade)
#     if dezena == 1:
#         print(f"{numero} = {dic_numeros[dezena][numero]}")
#     else:
#         if unidade == 0:
#             print(f"{numero} = {dic_numeros[dezena][1]}")
#         elif unidade == 1:
#             print(f"{numero} = {dic_numeros[dezena][1]} e {dic_numeros[unidade][unidade]}")
#         else:
#             print(f"{numero} = {dic_numeros[dezena][1]} e {dic_numeros[unidade][0]}")
# else:
#     if numero == 1:
#         print(f"{numero} = {dic_numeros[numero][numero]}")
#     else:
#         print(f"{numero} = {dic_numeros[numero][0]}")

# 11-Jogo de Forca.
# Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto
# e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado
#      Digite uma letra: A
#     -> Você errou pela 1ª vez. Tente de novo!
#
#     Digite uma letra: O
#     A palavra é: _ _ _ _ O
#
#     Digite uma letra: E
#     A palavra é: _ E _ _ O
#
#     Digite uma letra: S
#     -> Você errou pela 2ª vez. Tente de novo!



# 12-Valida e corrige número de telefone.
# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos,
# acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador
#     Valida e corrige número de telefone
#     Telefone: 461-0133
#     Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#     Telefone corrigido sem formatação: 34610133
#     Telefone corrigido com formatação: 3461-0133

# 13-Jogo da palavra embaralhada.
# Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela,
# informando se o usuário ganhou ou perdeu o jogo.

# 14-Leet spek generator.
# Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
# como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337.
# O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet,
# sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo.
# Pesquise sobre as principais formas de traduzir as letras.
# Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
