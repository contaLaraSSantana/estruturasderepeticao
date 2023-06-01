# 4.Escreva um programa que mostre todos os números entre 5 e 100 que são
# divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos
# em sequência. E no final mostre a quantidade de números.

qn = 0
for n in range(5,101):
    if n % 7 == 0 and n % 5 != 0 :
        qn += 1
        print(n)
print("Quantidade de números:",qn)

#5. Desenvolva um programa que leia o nome, idade e sexo de 8 pessoas.
#No final do programa mostre:
#-Qual o nome do homem mais velho
#-Quantas mulheres tem menos de 20 anos

idadevelho = 0
nomevelho = ''
mulheres20 = 0
for n in range(0, 9):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo: '))
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    elif sexo == 'F' and idade <= 20:
        mulheres20 += 1
print('O mais velho se chama: ',nomevelho)
print('Mulheres que tem menos de 20 anos: ',mulheres20)