#!/usr/bin/env python3
# ===========================================================================
#  Exercício 011 Aula 07 - Pintando Parede
#  Faça um programa que leia a largarua de aaltura de uma parede em metros,
#  calcule sua área e a quantidade de tinta necessáira apra priná-la,
#  sabendo que cada litro de tinta pinta uma área de 2m².
# ===========================================================================


# 1L -> 2m²

altura = float(input('Qual a altura de sua parede? '))
comp = float(input('Qual o comprimento de sua parede?'))

area = (altura * comp)
qtd = (area / 2)

print()
print('As dimensões de sua parede são: {:.2f}x{:.2f}m. possuindo área de {}m²'
      .format(altura, comp, area))


# Tabela de conversão

print(f'''
    {'='*50}
    Altura     Comprimento      Área        Quantidade
    {altura:.2f}m      {comp:.2f}m            {area:.2f}m²      {qtd:.2f}L
    {'='*50}

     '''

      )
