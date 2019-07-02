#!/usr/bin/env python3
# ===========================================================================
#  Exercício 008 Aula 07 - Conversor de Medidas
#  Escreva um programa que leia um valor em metros e o exiba convertido
#  em centímetros e milímetros.
# ===========================================================================

# Escala de conversão
# -------------------------------------------------------------------
# km        hm        dam        m        dm        cm        mm
# 0,001     0,01      0,1        1        10        100       1000
# -------------------------------------------------------------------

# Vamos aproveitar e mostrar todas as medidas relacionadas seguindo a tabela.

medida = float(input('Digite uma distância em metros: '))

km = (medida / 1000)
hm = (medida / 100)
dam = (medida / 10)
dm = (medida * 10)
cm = (medida * 100)
mm = (medida * 1000)

print('\n \nDistância de referência: {} em [metros]'.format(medida))


# Vamos colocar isso dentro de uma table para facilitar a visualização

print(f'''

      {'-'*70}
       km        hm        dam        m        dm        cm        mm
       {km}     {hm}      {dam}        {medida}      {dm}      {cm}     {mm}
      {'-'*70}


'''
      )


print(

    '{}m podem ser convertidos para as seguintes medidas: \n\n'
    f'''{'-'*10}''' '\n'
    '{:.0f} mm \n'
    '{:.0f} cm \n'
    '{:.0f} dm \n'
    '{} dam \n'
    '{} hm \n'
    '{} km \n'
    f'''{'-'*10}''' '\n'
    .format(medida, mm, cm, dm, dam, hm, km)
)
