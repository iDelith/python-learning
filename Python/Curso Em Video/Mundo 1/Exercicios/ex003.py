# Exercício #003 - Aula 06
# Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
somanum = num1 + num2

msg = 'Os números digitados foram: {} e {}\n Sua soma é: {}'.format(
    num1, num2, somanum)

print(msg)
