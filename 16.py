horas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
percentual_desconto = float(input("Digite o percentual de desconto (não precisa ser em dedcimal): "))
dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas * valor_hora
desconto = salario_bruto * (percentual_desconto/100)
salario_liquido = salario_bruto - desconto
salario_liquido += dependentes * 100

print(f"O salário líquido é: R$ {salario_liquido:.2f}")
