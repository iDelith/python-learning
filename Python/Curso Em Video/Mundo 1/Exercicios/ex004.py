# ===========================================================================
#  Exercício 004 Aula 06 - Dissecando uma variável
#  Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo
#  primitivo e todas as informações possíves sobre ele.
# ===========================================================================


vartype = input('Digite algo: ')


print('Vamos verificar quais as características do valor digitado. \n \n')
print('O tipo primitivo desse valor é: ', type(vartype))
print('É um valor apenas numérico?', vartype.isnumeric())
print('É um valor apenas afabético?', vartype.isalpha())
print('É um valor alfanumérico?', vartype.isalnum())
print('É um valor apenas maiúsculo?', vartype.isupper())
print('É um valor apenas minúsculo?', vartype.islower())
print('É um valor capitalizado?', vartype.istitle())
print('É uma série que contém apenas espaços?', vartype.isspace())

print('\n \nEssa é a análise obtida do que foi digitado. \n ')
