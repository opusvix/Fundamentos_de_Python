"""
Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar.
A mensagem na tela deverá seguir o seguinte formato:

"O número [número] é [par/ímpar]"
"""

number = int(input("Enter your number: "))

if number % 2 == 0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")
