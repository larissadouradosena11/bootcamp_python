## Faça um programa que peça dois números inteiros e imprima a divisão do primeiro pelo segundo:

numero_01 = int(input("Insira um número inteiro:"))
if isinstance(numero_01, int):
    numero_02 = int(input("Insira outro número inteiro:"))
if isinstance(numero_02, int):
    def calculadora_divisao(numero_01, numero_02):
        try:
            resultado = numero_01 // numero_02
            return resultado
        except:
            print("integer division or modulo by zero")
            return None
        
    resultado_divisao = calculadora_divisao(numero_01, numero_02)

    if resultado_divisao is not None:
        print(f"A divisão de {numero_01} por {numero_02} é: {resultado_divisao:.2f}")
else:
    print("A variável não é inteira")

## Faça um programa que calcule a área de um circulo, recebendo o raio como entrada:
import math

raio_do_circulo = float(input("Digite o raio:"))

def area_do_circulo(raio_do_circulo):
    resultado = math.pi * raio_do_circulo ** 2
    return resultado

area_final = area_do_circulo(raio_do_circulo)
print(f"A area do circulo com raio {raio_do_circulo}: {area_final:.2f}")

## Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e ano separadamente

data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")

def lista_dia_mes_ano(data):
    lista_final = data.split("/")
    return lista_final

lista_final = lista_dia_mes_ano(data_do_usuario)

print(f"O dia digitado é: {lista_final[0]}.")
print(f"O mês digitado é: {lista_final[1]}.")
print(f"O ano digitado é: {lista_final[2]}.")

