#3. Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
#• idade média das mulheres
#• idade média dos homens
#• idade média do grupo

idademulheres = 0
idadehomens = 0
idadegrupo = 0
quantmulher = 0
quanthomens = 0

for n in range(1, 11):
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo(F-Feminino e M-masculino): '))
    if sexo == 'F':
        idademulheres += idade
        quantmulher += 1
    elif sexo == 'M':
        idadehomens += idade
        quanthomens += 1

    idadegrupo += idade

mdmulheres = idademulheres / quantmulher
mdhomens = idadehomens / quanthomens
mdgrupo = idadegrupo / 10

print('A idade média das mulheres é: ', mdmulheres)
print('A idade média dos homens é: ', mdhomens)
print('A idade média do grupo é: ', mdgrupo)
