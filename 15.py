import math 

cateto1 = float(input("digite o valor do primeiro cateto oposto: "))
cateto2 = float(input("digite o valor do segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"O valor da hipotenusa e: {hipotenusa}")