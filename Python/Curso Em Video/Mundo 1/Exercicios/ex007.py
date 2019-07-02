#!/usr/bin/env python3
# ===========================================================================
#  Exercício 007 Aula 07 - Média Aritmética
#  Desenvolva um programa que leia as duas notas de um aluno, calcule e
#  mostre a sua média.
# ===========================================================================

n1 = float(input('Digite a nota da 1ª prova: '))
n2 = float(input('Digite a nota da 2ª prova: '))

# Utilizando uma nova variável para um caso de proof-error, onde podemos comparar
# a nota real do aluno e seu valor arredondado se necessário.
# +1 to scalability !


media = (n1 + n2) / 2
rmedia = round(media, 2)

# Adicionando também o uso do método round para arrendodamentos de 2 casas decimais
print('A média de notas do aluno em questão é: {}'.format(rmedia))
