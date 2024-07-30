## Toda variável é um espaço na memória do computador, quando fazemos lanche = hamburguer a palavra "hamburguer" será armazenada no espaço da memória reservado para a variável lanche
## caso eu faça lanche = suco, o que acontecerá é que o espaço da memória que antes estava ocupada pelo "hamburguer" será substituida por "suco". Como estamos falando de uma variavel
## simples, há apenas um espaço em memória. E aqui surge a necessidade de termos mais espaço dentro da variável e isso é possível sim e uma das formas de fazermos isso com python é 
## usando as tuplas.

lanche = "hamburguer" # variável simple

lanche = ("hamburguer", "suco", "pizza", "pudim") # variável composta - Tupla

lanche_split = lanche[1]
print(lanche)

tamanho = len(lanche)
print(tamanho)

# eu já tenho a variável lanche mas não tenho a variável c, logo o python vai criar uma variável simples chamada c. Como for é uma estrutura de repetição ele só parará quando 
# acabar a tupla

for c in lanche:
    print(c)

lanche = ("hamburguer", "suco", "pizza", "pudim","batata frita")

for cont in range(0, len(lanche)):
    print(lanche[cont])

## As tuplas são imutáveis

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(2))



############################################################################DESAFIO############################################################################

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez'
           ,'onze','doze','treze','quartorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input("Digite um número entre 0 e 20:"))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ",end='')
print(f"Você digitou o número {numeros[num]}")




