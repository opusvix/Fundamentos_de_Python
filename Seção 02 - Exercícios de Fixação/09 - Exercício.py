"""
Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados.
Considere as seguintes informações:

Triângulo equilátero: todos os lados possuem o mesmo tamanho;

Triângulo escaleno: todos os lados possuem medidas diferentes;

Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.
"""
sideA = float(input('Side A: '))
sideB = float(input('Side B: '))
sideC = float(input('Side C: '))

if sideA == sideB == sideC:
    print('The triangle is equilateral.')
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print('The triangle is isosceles.')
else:
    print('The triangle is scalene.')
