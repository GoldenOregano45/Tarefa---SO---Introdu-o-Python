alimento_kg = float(input("Digite a quantidade de alimento em kg: "))
alimento_g = alimento_kg * 1000
dias = alimento_g / 50

print(f"o alimento vai durar: {dias:.0f} dias")