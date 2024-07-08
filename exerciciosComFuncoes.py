import random


# 1-Faça um programa para imprimir:
#         1
#         2   2
#         3   3   3
#         .....
#         n   n   n   n   n   n  ... n
#     para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

# def imprima (n):
#     i = 1
#     while i <= n:
#         x = 1
#         while x <= i:
#             print(f"{i}", end=" ")
#             x += 1
#         print("")
#         i += 1
# n = int(input("Digite um número inteiro: "))
# imprima(n)

# 2-Faça um programa para imprimir:
#         1
#         1   2
#         1   2   3
#         .....
#         1   2   3   ...  n
#     para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

# def imprima_n (n):
#     i = 1
#     while i <= n:
#         x = 1
#         while x <= i:
#             print(f"{x}", end=" ")
#             x += 1
#         print()
#         i += 1
#     return
# n = int(input("Digite um número inteiro: "))
# imprima_n(n)

# 3-Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# def soma_tres (n1, n2, n3):
#     soma = n1 + n2 + n3
#     return soma
# num1 = 2
# num2 = 4
# num3 = 8
# soma = soma_tres(num1, num2, num3)
# print(soma)

# 4-Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

# def positivo_ou_negativo (n):
#     arg = ""
#     if n >= 0:
#         arg = "P"
#     else:
#         arg = "N"
#     return arg
# numero = -1
# print(positivo_ou_negativo(numero))

# 5-Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item
# antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

# def somaImposto (taxaImposto, custo):
#     custo = custo * ((taxaImposto/100) + 1)
#     return custo
# taxa = 15
# custo = 100
# print(f"{somaImposto(taxa, custo):.2f}")

# 6-Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
# o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M.
# e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

# def conversao_horas(hora):
#     hora_convertida = 0
#     if hora == 24:
#         hora_convertida = 0
#     elif 12 < hora < 24:
#         hora_convertida = hora - 12
#     else:
#         hora_convertida = hora
#     return hora_convertida
#
# def turno (hora):
#     turno = ""
#     if 12 < hora < 24:
#         turno = "P.M"
#     else:
#         turno = "A.M"
#     return turno
#
# hora = " "
# while hora != -1:
#     print(f"Digite -1 para encerrar o programa!")
#     hora = int(input("Digite um número inteiro para as horas: "))
#     if hora != -1:
#         if 0 <= hora <= 24:
#             minuto = int(input("Digite um número inteiro para os minutos: "))
#             if 0 <= minuto < 60:
#                 print(f"{hora}:{minuto} = {conversao_horas(hora)}:{minuto} {turno(hora)}")
#             else:
#                 print("Minuto inválido")
#         else:
#             print("Hora inválida")

# 7-Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para
# a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
# outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
# e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

# def valorPagamento (prestacao, dias):
#     if dias_de_atraso > 0:
#         juros = (dias * 0.001) * prestacao  # juros de 0,1% por dia de atraso
#         prestacao = round((prestacao * 1.03) + juros, 2)  # multa de 3%
#     return prestacao
#
# valor_prestacao = ""
# relatorio = []
# while valor_prestacao != 0:
#     valor_prestacao = float(input("\nDigite o valor da prestação: "))
#     if valor_prestacao != 0:
#         dias_de_atraso = int(input("Digite o números de dias de atraso: "))
#         valor_prestacao = valorPagamento(valor_prestacao, dias_de_atraso)
#         relatorio.append(valor_prestacao)
#         print(f"Valor a pagar: R$ {valor_prestacao}")
#
# print(f"\n{relatorio}")
# print("Relatório do Dia")
# print(f"Número de prestações: {len(relatorio)}\n"
#       f"Total das prestações: R$ {sum(relatorio):.2f}")

# 8-Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

# def conta_digitos (n):
#     digitos = len(str(n))
#     return digitos
# numero = int(input("Digite um número inteiro: "))
# print(f"{conta_digitos(numero)}")

# 9-Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

# def numero_reverso (n):
#     reverso = 0
#     while n > 0:
#         resto = n % 10
#         reverso = (reverso * 10) + resto
#         n = int(n /10)
#     return reverso
# numero = int(input("Digite um número inteiro: "))
# print(f"Número digitado = {numero}\n"
#       f"Número reverso = {numero_reverso(numero)}")

# 10-Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando
# os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

# def joga_dados ():
#     a = 1
#     b = 6
#     jogadas = []
#     for i in range(2):
#         dado = random.randint(a,b)
#         jogadas.append(dado)
#     return sum(jogadas)
#
# def verifica_jogadas (dic_jogadas, jogador):
#     info = []
#     ponto = dic_jogadas[jogador][1]
#     partida = dic_jogadas[jogador][2]
#     # print(jogador, ponto, partida)
#     jogo = joga_dados()
#     primeiro_acerto = jogo
#     print(f"Primeiro acerto = {jogo}")
#     if partida == 0:
#         if jogo == 7 or jogo == 11:
#             print("Ganhou de primeira!")
#
#             ponto = jogo
#             partida += 1
#         elif jogo == 2 or jogo == 3 or jogo == 12:
#             print("Perdeu de primeira :(")
#             ponto = jogo
#             partida += 1
#         else:
#             ponto = jogo
#             partida += 1
#             primeiro_acerto = jogo
#             print("Somou ponto")
#             while ponto != 7 and ponto != (2 * primeiro_acerto):
#                 jogo = joga_dados()
#                 print(jogo)
#                 if jogo == 7:
#                     print("Perdeu porque tirou 7")
#                     ponto = jogo
#                 elif jogo == ponto:
#                     print("Tirou o mesmo número novamente. Objetivo alcançado! ")
#                     ponto += ponto
#                     # partida += 1
#                 else:
#                     print("Jogue novamente")
#                 partida += 1
#
#     info.append(primeiro_acerto)
#     info.append(ponto)
#     info.append(partida)
#     dic_jogadas[jogador] = info
#     return dic_jogadas
#
# info_jogo = {}
# info_iniciais = [0,0,0]
# jogador = " "
# while len(info_jogo) < 12 and jogador != "":
#     jogador = input("Informe o nome do Jogador: ").upper()
#     if jogador != "":
#         info_jogo[jogador] = info_iniciais
#         print(f"{verifica_jogadas(info_jogo, jogador)}\n")
#
# print("Resultado do Jogo! ")
# for i in info_jogo:
#     if info_jogo[i][2] == 1:
#         if info_jogo[i][1] == 7 or info_jogo[i][1] == 11:
#             print(f"Jogador(a): {i} - Ganhou de primeira!\n"
#                   f"Tirou {info_jogo[i][1]} na primeira rodada.")
#         if info_jogo[i][1] == 2 or info_jogo[i][1] == 3 or info_jogo[i][1] == 12:
#             print(f"Jogador(a): {i} - Perdeu de primeira!\n"
#                   f"Tirou {info_jogo[i][1]} na primeira rodada.")
#     else:
#         if info_jogo[i][1] == 7:
#             print(f"Jogador(a): {i} - Perdeu após {info_jogo[i][2]} rodadas.\n"
#                   f"Tirou o {info_jogo[i][1]} após o primeiro ponto ser igual a {info_jogo[i][0]}")
#         else:
#             print(f"Jogador(a): {i} - Ganhou após {info_jogo[i][2]} rodadas.\n"
#                   f"Tirou o {info_jogo[i][0]} novamente e somou {info_jogo[i][1]} pontos.")
#     print("\n")

# 11-Data com mês por extenso.
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string
# no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

# def transforma_data (dt):
#     data_extenso = " "
#     if len(data) == 10 and data[2:3] == "/" and data[5:6] == "/":
#         if int(data[6:]) > 0:
#             if int(data[3:5]) == 2:
#                 bissexto = int(data[6:]) % 4
#                 if bissexto == 0:
#                     if 0 < int(data[:2]) <= 29:
#                         data_extenso = f"{data[:2]} de {meses[int(data[3:5])]} de {data[6:]}"
#                     else:
#                         data_extenso = (f"Data inválida! O ano {data[6:]} é bissexto.\n"
#                                         f"E o mês de {meses[int(data[3:5])]} tem no máximo 29 dias.")
#                 else:
#                     if 0 < int(data[:2]) <= 28:
#                         data_extenso = f"{data[:2]} de {meses[int(data[3:5])]} de {data[6:]}"
#                     else:
#                         data_extenso = (f"Data inválida! O ano {data[6:]} não é bissexto.\n"
#                                         f"E o mês de {meses[int(data[3:5])]} tem no máximo 28 dias.")
#             else:
#                 if 0 < int(data[3:5]) <= 12:
#                     if int(data[3:5]) == 4 or int(data[3:5]) == 6 or int(data[3:5]) == 9 or int(data[3:5]) == 11:
#                         if 0 < int(data[:2]) <= 30:
#                             data_extenso = f"{data[:2]} de {meses[int(data[3:5])]} de {data[6:]}"
#                         else:
#                             data_extenso = f"Data inválida! O mês de {meses[int(data[3:5])]} tem no máximo 30 dias."
#                     else:
#                         if 0 < int(data[:2]) <= 31:
#                             data_extenso = f"{data[:2]} de {meses[int(data[3:5])]} de {data[6:]}"
#                         else:
#                             data_extenso = f"Data inválida! O mês de {meses[int(data[3:5])]} tem no máximo 31 dias."
#                 elif int(data[3:5]) == 0:
#                     data_extenso = "Mês igual a zero não é válido."
#                 else:
#                     data_extenso = "Data inválida! Temos no máximo 12 meses no ano."
#         else:
#             data_extenso = "Só é válido ano maior que zero!"
#     else:
#         data_extenso = "Formato da data inválido!"
#     return data_extenso
#
# meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
#          9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
#
# data = input("Digite uma data no seguinte formato DD/MM/AAAA: ")
# print(data)
# print(transforma_data(data))

# 12-Embaralha palavra.
# Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
# de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
# independentemente de como foram digitados.

# def embaralha_palavra (palavra):
#     palavra = palavra.lower()
#     posicoes = []
#     embaralhada = ""
#     i = 0
#     while i < len(palavra):
#         a = 0
#         b = len(palavra) - 1
#         x = random.randint(a, b)
#         if x not in posicoes:
#             posicoes.append(x)
#             embaralhada = embaralhada + palavra[x]
#             i += 1
#     return embaralhada
#
# palavra = input("Digite uma palavra: ")
# print(palavra)
# print(embaralha_palavra(palavra))

# 13-Desenha moldura.
# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1
# e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores
# dentro da faixa de forma elegante.
# +-+
# | |
# +-+

# def moldura (linhas, colunas):
#     caracteres = ["+", "-", "|"]
#     print(caracteres[0], end="")
#     c = 1
#     while c <= colunas:
#         print(caracteres[1], end="")
#         c += 1
#     print(caracteres[0])
#     l = 1
#     while l <= linhas:
#         print(caracteres[2], end="")
#         print(f"{caracteres[2]:>{colunas + 1}}")
#         l += 1
#     print(caracteres[0], end="")
#     c = 1
#     while c <= colunas:
#         print(caracteres[1], end="")
#         c += 1
#     print(caracteres[0])
#     return
#
# print("Vamos desenhar um retâgulo!\n"
#       "Os valores devem ser no mínino 1 e no máximo 20.")
# linhas = int(input("Digite o número de linhas: "))
# colunas = int(input("Digite o número de colunas: "))
#
# a = 1
# b = 20
# if linhas < 0 or linhas > 20:
#     linhas = random.randint(a, b)
# if colunas < 0 or colunas > 20:
#     colunas = random.randint(a, b)
#
# # print(linhas, colunas)
# moldura(linhas, colunas)

# 14-Quadrado mágico.
# Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas,
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
#     8  3  4
#     1  5  9
#     6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes = []
uma_combinacao = []

for pt in numeros:
    for st in numeros:
        for tt in numeros:
            uma_combinacao.append(pt)
            if st not in uma_combinacao:
                uma_combinacao.append(st)
            if tt not in uma_combinacao:
                uma_combinacao.append(tt)
            if len(uma_combinacao) == 3 and sum(uma_combinacao) == 15:
                # print(uma_combinacao)
                combinacoes.append(uma_combinacao)
            uma_combinacao = []
print(f"{combinacoes} \n"
      f"{len(combinacoes)}")

repeticao_numeros = {}
for i in combinacoes:
    for x in i:
        repeticao_numeros[x] = 0
for i in combinacoes:
    for x in i:
        repeticao_numeros[x] = repeticao_numeros[x] + i.count(x)
ordenado = {}
for i in sorted(repeticao_numeros, key=repeticao_numeros.get, reverse=True):
    ordenado[i] = repeticao_numeros[i]
print(ordenado)

quadro_magico = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in combinacoes:
    # print(len(quadro_magico))
    # if len(quadro_magico) <= 3:
    if 5 in c:
        if quadro_magico[1][0] == 0:
            quadro_magico[1] = c
val = False
for c in combinacoes:
    if c not in quadro_magico:
        for i in c:
            for n in quadro_magico:
                if i in n:
                    val = True
        if val == False:
            if quadro_magico[0][0] == 0:
                quadro_magico[0] = c
            else:
                if quadro_magico[2][0] == 0:
                    quadro_magico[2] = c
        else:
            val = False

for c in quadro_magico:
    for i in c:
        print(i, end=" ")
    print()

for i in combinacoes:
    if 6 in i:
        print(i, end=" ")