"""
Escreva um programa que solicite o nome e o sobrenome do usuário.
Ao final o programa deverá apresentar o nome completo do usuário na tela.
"""

first_name = input("Enter your first name: ").strip().title()
last_name = input("Enter your last name: ").strip().title()

print(f"{first_name} {last_name}")
