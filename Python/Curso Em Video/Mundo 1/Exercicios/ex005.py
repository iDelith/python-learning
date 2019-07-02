#!/usr/bin/env python3
# ===========================================================================
#  Exercício 005 Aula 07 - Antecessor e Sucessor
#  Faça um programa que leia um número inteiro e mostre na tela o seu
#  sucessor e antecessor.
# ===========================================================================


# Utilizando-se de duas variáveis para armazenar os dados

n = int(input('Digite um número: '))

nant = n - 1
nsuc = n + 1

print(

    '''\nO número digitado foi: {}
O número antecessor é: {}
O número sucessor é: {}
'''.format(n, nant, nsuc)
)

# Utilizando-se dos atributos de incrementação e uma única variável

num = int(input("Digite um novo número para análise: "))

print('\nSeu novo número é {}, seu antecessor é {} e seu sucessor é {}.\n'.format(
    num, (num - 1), (num + 1)))
