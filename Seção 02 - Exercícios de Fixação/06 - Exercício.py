"""
Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado.
Considere a possibilidade de o usuário digitar dois números iguais.
"""

number_01 = int(input("Enter your first number: "))
number_02 = int(input("Enter your second number: "))

if number_01 > number_02:
    print(f'Number {number_01} greater then {number_02}')
elif number_01 == number_02:
    print(f"Number {number_01} is equal {number_02}")
else:
    print(f"Number {number_01} is smaller {number_02}")
