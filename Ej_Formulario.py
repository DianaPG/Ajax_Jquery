##Introducir los valores A, B y C: 
###Si A/B>30, calcular e imprimir A/C * B^3 
###Si A/B<=30, calcular e imprimir 2^2+4^2+6^2+...+30^2
a = input('Primer valor: ')
b = input('Segundo valor: ')
c = input('Tercer valor: ')
n = 2
suma = 0
sumas = 0
if a/b > 30:
    suma = a/c*b**3
    print suma
if a/b <= 30:
    while n <= 30:
        sumas += n**2
        n += 2
    print sumas