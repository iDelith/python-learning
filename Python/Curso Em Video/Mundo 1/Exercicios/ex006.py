# ===========================================================================
#  Exercício 006 Aula 07 - Operadores Aritiméticos
#  Crie um algorítmo que leia um número e mostre o seu dobro, triplo
#  e raíz quadrada.
# ===========================================================================


def operacao():
    ''' Quero chamar essa função e mostrar na tela as operações '''
    num = int(input('Digite um número: '))
    dobro = num * 2
    triplo = num * 3
    rq = round(num**0.5)
    return


def show():
    ''' Função responsável por mostrar na tela'''
    # print((operacao(num) * 2), (operacao(num) * 3),
    #       round((operacao(num)**0.5)))
    dobro = operacao().dobro
    triplo = operacao().triplo
    rq = round(operacao().rq)
    print('Dobro:', dobro)
    print('Triplo:', 3)
    print('Raíz Quadrada:', 4)
    return


operacao()
show()
