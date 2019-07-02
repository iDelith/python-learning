#!/usr/bin/env python3
# ===========================================================================
#  Exercício 010 Aula 07 - Conversor de Moedas
#  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
#  mostre quandos dólares ela pode comprar.
#
#  Considere U$1,00 = R$3,27
# ===========================================================================

saldo = float(input('Quantos reais você tem na carteira? R$'))
dolar = (saldo / 3.27)

print('\nAh, você tem R${:.2f}...'.format(saldo))
print('Então com R${:.2f} você pode comprar até U${:.2f}'.format(saldo, dolar))
print()


# OUTPUT

# Quantos reais você tem na carteira? R$20

# Ah, você tem R$20.00...
# Então com R$20.00 você pode comprar até U$6.12
