import math

a = float(input("digite o coeficiente de A: "))
b = float(input("digite o coeficiente de B: "))
c = float(input("digite o coeficiente de C: "))

delta = b**2 - 4 *a*c
if delta < 0:
    print ("nao existem raizes reais para a equacao")
else:
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)


    print (f"as raizes da equacao sao: x1 = {x1} e  x2 = {x2}")
