from ast import If


numero = int(input("Por favor ingrese un numero para ver si éste es multiplo de 5: "))
resultado= numero % 5
print(f'el residuo es: {resultado}')

#condicional simple en python
if(resultado==0):
    print("es multiplo de 5")
else:
    print("no es multiplo de 5 padresito llorelo")
print("fin del programa socio, si no hizo nada, llorelo")