nestedList = [["Francis", "English", 435],
              ["Larry", "Maths", 234],
              ["Nicole", "Biology", 986],
              ["Joey", "Physics", 562],
              ["Sam", "Computing", 12],
              ]

# Levando em consideração que a separação do print statement tem que ser descontada:
# len('First Name') = 10, porém a próxima iteração do separador obrigatoriamente
# colocará um ' ' na frente.
# Sendo assim, mentalmente o código será:
# [(lenTITULO -1) - LenNome] = espaço entre a tabulação


print("| First Name | Subject Chosen | Score |")

for i in nestedList:
    print('|', i[0], ' ' * (9 - len(i[0])), '|',
          i[1], ' ' * (13 - len(i[1])), '|',
          i[2], ' ' * (4 - len(str(i[2]))), '|'
          )
