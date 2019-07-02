print(
    '''
Vamos criar um box no terminal para estilização de tabelas

======================================
* Este teste será interpretado da    *
* seguinte maneira.                  *
* "Por favor insira seu texto aqui". *
======================================

'''
)

from terminaltables import SingleTable
# Instructions.
table_instance = SingleTable([['This will be a test required for\
    my purposes']], 'Instructions')
print(table_instance.table)
print()
