#!usr/bin/env python3
# ===========================================================================
#  Exercício 013 Aula 07 - Reajuste Salarial
#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
#  salário, com 15% de aumento.
# ===========================================================================

# Como anteriormente, vamos realizar a operação inversa nesse caso, aproveitando
# conceitos de scalability.


name = input('Qual o nome do seu funcionário?')
payment = float(input('Qual o salário atual de seu funcionário? R$'))
payment_raise = (15 / 100)
updated_payment = payment + (payment * payment_raise)

print()
print(f'Dessa maneira, o salário atualizado de {name} será totalizado'
      f' em R${updated_payment:.2f}.')
print()

# OUTPUT

# Qual o nome do seu funcionário?Joseph
# Qual o salário atual de seu funcionário? R$2830

# Dessa maneira, o salário atualizado de Joseph será totalizado em R$3254.50.
