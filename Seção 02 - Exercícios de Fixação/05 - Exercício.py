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
