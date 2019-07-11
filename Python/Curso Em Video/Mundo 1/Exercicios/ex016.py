#!usr/bin/env python3
# ===========================================================================
#  Exercício 016 Aula 08 - Quebrando um Número
#  Crie um programa que leia um número real qualquer pelo teclado e mostre
#  na tela a sua porção inteira.
# ===========================================================================

from math import trunc

num = float(input('Digite um número real: '))
num_int1 = int(num)
num_int2 = trunc(num)


# Vamos mostrar ambas as saídas:

print()
print('{:.2f}: Método1 -> {}, Método2 -> {}'.format(num, num_int1, num_int2))
print()


# OUTPUT

# Digite um número real: 6.123123124512

# 6.12: Método1 -> 6, Método2 -> 6
