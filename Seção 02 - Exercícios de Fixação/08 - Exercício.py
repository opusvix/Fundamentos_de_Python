"""
Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário.
Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida
(número entre 1 e 10) mostre na tela uma mensagem personalizada.

Exemplo: preço x categoria

* Categoria 1 - $ 0,5
* Categoria 2 - $ 11,3
* Categoria 3 - $ 17,5
* Categoria 4 - $ 33,97
* Categoria 5 - $ 103,47
* Categoria 6 - $ 44,67
* Categoria 7 - $ 12,55
* Categoria 8 - $ 14,87
* Categoria 9 - $ 98,12
* Categoria 10 - $ 131,4
"""

category = int(input("Enter the category number: "))

if category == 1:
    print("The product price is: $ 0,5")
elif category == 2:
    print("The product price is: $ 11,3")
elif category == 3:
    print("The product price is: $ 17,5")
elif category == 4:
    print("The product price is: $ 33,97")
elif category == 5:
    print("The product price is: $ 103,47")
elif category == 6:
    print("The product price is: $ 44,67")
elif category == 7:
    print("The product price is: $ 12,55")
elif category == 8:
    print("The product price is: $ 14,87")
elif category == 9:
    print("The product price is: $ 98,12")
elif category == 10:
    print("The product price is: $ 131,4")
else:
    print("Invalid option.")
