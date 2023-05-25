import random

# Definir os valores das colunas e linhas
colunas = ['Header', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
linhas = ['Fernando', 'Gabriel', 'Igor', 'Rodrigo']

# Criar a tabela vazia
tabela = [['' for _ in range(len(colunas))] for _ in range(len(linhas))]

# Preencher a tabela com "X" respeitando as restrições
for i in range(len(tabela)):
    linha = tabela[i]
    colunas_restantes = list(range(len(colunas)))
    random.shuffle(colunas_restantes)

    for j in range(len(linha)):
        coluna_index = colunas_restantes[j]
        linha[coluna_index] = 'X'

# Imprimir a tabela
print('+---------+---------+---------+---------+---------+---------+')
print('| ' + ' | '.join(colunas) + ' |')
print('+---------+---------+---------+---------+---------+---------+')

for linha in tabela:
    print('| ' + ' | '.join(linha) + ' |')
    print('+---------+---------+---------+---------+---------+---------+')
