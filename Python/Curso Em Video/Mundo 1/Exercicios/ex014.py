#!usr/bin/env python3
# ===========================================================================
#  Exercício 014 Aula 07 - Conversor de Temperaturas
#  Escreva um programa que converta uma temperatura digitada em ºC e
#  converta para ºF
# ===========================================================================


# 1,8 * C + 32

temp_degree = float(input('Qual a temperatura em ºC? '))
temp_ft = (temp_degree * 1.8) + 32

print('A temperatura de {}ºC equivale à {}ºF'.format(temp_degree, temp_ft))

# OUTPUT

# Qual a temperatura em ºC? 1
# A temperatura de 1.0ºC equivale à 33.8ºF
