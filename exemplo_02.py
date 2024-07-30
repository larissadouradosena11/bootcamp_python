## Exercício 1: Verificação da qualidade de dados
# Vacê está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para 'quantidade' e 'preço'.
# Escreva um programa que verifique esses campos e imprima "Dados válidados" se ambos
# forem positivos ou "Dados inválidos" caso contrário

quantidade = 40
preco = -20

if quantidade > 0 and preco > 0:
    print("Dados válidados")
else:
    print("Dados inválidos")