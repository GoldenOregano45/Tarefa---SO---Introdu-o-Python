tempo = float(input("Digite o tempo em horas: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))

distancia = tempo * velocidade_media
litros_consumidos = distancia / 12

print(f"A distância percorrida é: {distancia} km")
print(f"Os litros consumidos foram: {litros_consumidos:.2f} L")