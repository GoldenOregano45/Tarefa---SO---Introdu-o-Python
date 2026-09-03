ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento
idade_futura = idade + 17

print(f"A idade do indivíduo é: {idade} anos")
print(f"Idade daqui a 17 anos será de {idade_futura} anos")