"""
Escreva um programa que peça o nome e a idade do usuário.
Caso a idade do usuário seja maior ou igual a 18 anos apresente a seguinte mensagem:
"Seja bem-vindo ao nosso site [nome]!"; caso contrário, apresente a seguinte mensagem:
"Você não pode acessar nosso site [nome].".
"""

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Welcome to our website {name.strip().title()}!")
else:
    print(f'You cannot access our website {name.strip().title()}.')
