#!/usr/bin/env python3
# ===========================================================================
#  Exercício 009 Aula 07 - Tabuada
#  Faça um programa que leia um número inteiro qualquer e mostre na tela
#  sua tabuada.
# ===========================================================================

# Tabuada básica utilizando apenas a função print

num = int(input('Digite um número para verificar a tabuada: '))


print(f'''

    {'='*40}
      Utilizando apenas o método print():
    {'='*40}

    '''
      )


print('-' * 20)
print('{} x {:2} = {}'.format(num, 1, num * 1))
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {:2} = {}'.format(num, 10, num * 10))
print('-' * 20)


# Vamos tentar fazer essa mesma tabuada utilizando for loop

print(f'''

    {'='*40}
      Utilizando o método for-loop:
    {'='*40}

    '''
      )



print('-' * 20)

for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num * i))

print('-' * 20)

# OUTPUT

# Digite um número para verificar a tabuada: 9


#     ========================================
#       Utilizando apenas o método print():
#     ========================================


# --------------------
# 9 x  1 = 9
# 9 x  2 = 18
# 9 x  3 = 27
# 9 x  4 = 36
# 9 x  5 = 45
# 9 x  6 = 54
# 9 x  7 = 63
# 9 x  8 = 72
# 9 x  9 = 81
# 9 x 10 = 90
# --------------------


#     ========================================
#       Utilizando o método for-loop:
#     ========================================


# --------------------
# 9 x  1 = 9
# 9 x  2 = 18
# 9 x  3 = 27
# 9 x  4 = 36
# 9 x  5 = 45
# 9 x  6 = 54
# 9 x  7 = 63
# 9 x  8 = 72
# 9 x  9 = 81
# 9 x 10 = 90
# --------------------

