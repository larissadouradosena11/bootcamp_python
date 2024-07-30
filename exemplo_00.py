# Captura as entradas do usuário
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
bonus = float(input("Digite seu último bônus: "))

# Define a função para calcular o bônus
def calculadora_bonus(salario, bonus):
    bonus_calculado = 1000 + (salario * bonus)
    return bonus_calculado

# Usa a função e imprime o resultado
bonus_total = calculadora_bonus(salario, bonus)
print(f"O bônus total calculado para {nome} é: {bonus_total:.2f}")
