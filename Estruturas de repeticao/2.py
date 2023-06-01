# 1. Construa um programa em Python utilizando os comandos aprendidos até
# agora para encontrar todos os números pares entre 1 e 100. E no final mostre
# a quantidade de números

pares = 0
for par in range(1,101):
    if par % 2 == 0:
        pares += 1
print("Existem",pares,"números pares entre 1 e 100")

# Faç'a um programa em linguagem Python que recebe a temperatura de z cliente e imprima
# a mensagem de se a temperatura esta normal (menor que 37,2 C) ou está em estado febril
# (37,3 C a 38 C ) ou com febre (38 C a 39 C) e com febre alta(acima 39 C).
# No final mostre a quantidade de pessoas analisadas e a média de temperatura.

qc = int(input('Quantidade de clientes que você irá analisar:'))
soma = 0

for n in range(1,qc+1):
    t = float(input('Digite a temperatura:'))
    soma += t
    if t <= 37.2:
        print('O paciente está em estado normal')
    elif t >= 37.3 and t < 38:
        print('O paciente está em estado febril')
    elif t >= 38 and t <= 39:
        print('O paciente está em estado de febre')
    else:
        print('O paciente está em estado de febre alta')

media = soma/qc
print('A média das temperaturas é: ', media, 'E a quantidade de clientes analisados foi',qc)


