"""
Considere a tupla1 e responda as seguintes questões:

tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')

a) mostre na tela o tamanho desta tupla;

b) ordene a tupla e mostre o resultado na tela;

c) mostre na tela o número de ocorrências da string 'A';

d) mostre na tela o número de ocorrências da string 'B';

e) mostre na tela o índice da string 'X';

f) mostre na tela o último elemento da tupla1.
"""

tuple_01 = ('A', 'B', 'A', 'Z', 'Z', 'X', 'A', 'E', 'K', 'G', 'H')

# a) mostre na tela o tamanho desta tupla;
print(f'Tuple size:', len(tuple_01))

# b) ordene a tupla e mostre o resultado na tela;
print(sorted(tuple_01))

# c) mostre na tela o número de ocorrências da string 'A';
print("Number of occurrences of 'A'", tuple_01.count('A'))

# d) mostre na tela o número de ocorrências da string 'B';
print("Number of occurrences of 'B'", tuple_01.count('B'))

# e) mostre na tela o índice da string 'X';
print("String Index 'X'", tuple_01.index('X'))

# f) mostre na tela o último elemento da tupla1.
print(tuple_01[-1])
