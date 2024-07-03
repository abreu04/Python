# 1-Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos.
#     O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
#     O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

with open("enderecosIP.txt", "w") as arquivo:
    arquivo.write("200.135.80.9\n"
                  "192.168.1.1\n"
                  "8.35.67.74\n"
                  "257.32.4.5\n"
                  "85.345.1.2\n"
                  "1.2.3.4\n"
                  "9.8.234.5\n"
                  "192.168.0.256\n")

with open("enderecosIP.txt", "r") as arquivo:
    lista_ip = arquivo.readlines()

# print(lista_ip)

digito = ""
valido = []
ip_valido = []
ip_invalido = []

for i in lista_ip:
    for d in i:
        if d != "." and d != "\n":
            digito = digito + d
        else:
            if 0 <= int(digito) <= 255:
                valido.append(True)
            else:
                valido.append(False)
            digito = ""
    if False in valido:
        ip_invalido.append(i[:len(i)-1])
    else:
        ip_valido.append(i[:len(i)-1])
    valido = []

# print(ip_valido)
# print(ip_invalido)

with open("relatorioIp.txt", "w") as novo_arquivo:
    novo_arquivo.write("Endereços válidos:\n")
    for i in ip_valido:
        novo_arquivo.write(f"{i}\n")
    novo_arquivo.write("\nEndereços inválidos:\n")
    for i in ip_invalido:
        novo_arquivo.write(f"{i}\n")


# 2-A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet,
# ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa
# que gere um relatório, chamado "relatório.txt", no seguinte formato:
#
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
#
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
# deverá ser feita através de uma função separada, que será chamada pelo programa principal.
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal


# with open("usuarios.txt", "w") as usuarios:
#     usuarios.write("alexandre       456123789\n"
#                    "anderson        1245698456\n"
#                    "antonio         123456456\n"
#                    "carlos          91257581\n"
#                    "cesar           987458\n"
#                    "rosemary        789456125\n")
#
# def converte_bytes_megabytes (bytes):
#     espaco_mb = round(bytes / (2**20), 2)
#     return espaco_mb
# def calcula_percentual_espaco_usado (megaytes):
#     espaco_pct = round((megaytes * 100) / 2581.57, 2)
#     return espaco_pct
#
# with open("usuarios.txt", "r") as usuarios:
#     conteudo = usuarios.readlines()
#
# dic_usuarios = {}
# for i in conteudo:
#     espaco_usado = ""
#     nome = ""
#     verf = True
#     for l in i:
#         if l == " ":
#             verf = False
#         elif l != " " and verf == True:
#             nome = nome + l
#         else:
#             if l != "\n":
#                 espaco_usado = espaco_usado + l
#     dic_usuarios[nome] = int(espaco_usado)
#
# for i in dic_usuarios:
#     dados = []
#     mb = converte_bytes_megabytes(dic_usuarios[i])
#     perc = calcula_percentual_espaco_usado(mb)
#     dados.append(dic_usuarios[i])
#     dados.append(mb)
#     dados.append(perc)
#     dic_usuarios[i] = dados
# # print(dic_usuarios)
#
# with open("relatório.txt", "w") as info:
#     info.write("ACME Inc.               Uso do espaço em disco pelos usuários\n"
#                "------------------------------------------------------------------------\n"
#                "Nr.  Usuário        Espaço utilizado     % do uso\n")
#     x = 1
#     for i in dic_usuarios:
#         info.write(f"{str(x)}{" ":>4}{i}{dic_usuarios[i][1]:>{22-len(i)}} MB {dic_usuarios[i][2]:>17}%\n")
#         x += 1
