
# Teste de criação de uma Text UI para rodar no terminal, sem utilizar modulos.
# Aproveitando para treinar algorítmos variáveis

# Menu Entries

options_menu = '1 - Options'
invoke_menu = '2 - Invoker'
exit_menu = '3 - Exit'
limit_menu = 20


# UI Printing Block

print('+' + 'Welcome to Text-UI Module 1'.center(78, '-') + '+')
print('+' + '-' * 78 + '+')
print(

    '|' + 'HOME'.center((int(78 / 4))) + '|' +
    'EXERCISES'.center((int((78 / 4)))) + '|' + 1
    'GRADES'.center(int((78 / 4))) + '|' +
    'PROFILE'.center(int(((78 / 4) - 1))) + '|'
)

print('+' + '-' * 78 + '+')
print('|' + options_menu.center(78) + '|')
print(

    '|' + (invoke_menu.center(78 - (len(options_menu) - len(invoke_menu)) - 1)) +
    ' ' * (12 - len(invoke_menu)) + '|'
)

print(

    '|' + (exit_menu.center(78 - (len(options_menu) - len(exit_menu)) - 1)) +
    ' ' * (12 - len(exit_menu)) + '|'

)


for i in range(4):
    print('|' + ' ' * 78 + '|')
print('+' + '-' * 78 + '+')
