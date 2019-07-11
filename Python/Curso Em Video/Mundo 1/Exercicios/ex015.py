#!usr/bin/env python3
# ===========================================================================
#  Exercício 015 Aula 07 - Aluguel de Carros
#  Escreva um programa que pergunte a quantidade de KM percorridos por um
#  carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa $60 por dia e
#  R$0,15 por KM rodado.
# ===========================================================================


# Just the basic facts:

# y = ax + b
# y = km * 0.15 + 60 * dias

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual a kilometragem percorrida com o carro? '))
preço = (km * 0.15) + (dias * 60)

print()
print('Considerando as informações, o aluguel do carro será de R${:.2f}.'.format(preço))
print()

# OUTPUT

# Por quantos dias o carro foi alugado? 5
# Qual a kilometragem percorrida com o carro? 150

# Considerando as informações, o aluguel do carro será de R$322.50.
