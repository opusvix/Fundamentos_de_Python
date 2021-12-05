"""
O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa.
Escreva um programa que peça o nome, a idade , o peso e a altura do usuário.
Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.

IMC<17 - Muito abaixo do peso ideal

17<=IMC<18,5 - Abaixo do peso

18,5<=IMC<25 - Peso normal

25<=IMC<30 - Acima do peso

30<=IMC<35 - Obesidade I

35<=IMC<40 - Obesidade II (severa)

IMC>=40 - Obesidade III (mórbida)

Lembre que: IMC=massa/(altura*altura)
"""

print('Calculation of IMC\n')

name = (input("Enter your name: ")).strip().title()
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

imc = weight / (height * height)

if imc < 17:
    print('Much underweight!')
elif 17 <= imc < 18.5:
    print('Under weight')
elif 18.5 <= imc < 25:
    print('Normal weight')
elif 25 <= imc < 30:
    print('Overweight')
elif 30 <= imc < 35:
    print('Obesity I')
elif 35 <= imc < 40:
    print('Obesity II (severe)')
elif imc >= 40:
    print('Obesity III (morbid)')
