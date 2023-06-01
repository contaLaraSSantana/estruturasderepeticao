#Repetião, laço ou ciclo
#repetição de um conjunto de instruções por uma quantidade finita de vezes(for),ou então
#enquanto uma condição for verdadeira(while)

# for variavel in range(inicio,fim):
#print('Olá mundo')
#não precisa declarar a variável

for n in range(1,6):
    print('Olá mundo!')

#ele ignora o ultimo número

#for variavel in range(inicio,fim,passo)
#o passo é de qnt em qnt vai printar

for n in range(0,10,2):
    print(n)
print('FIM')

#subtrai 1
for n in range(10,0,-1):
    print(n)
print('FIM')

#escolher
i = int(input('Inicio:'))
f= int(input('Fim:'))
p= int(input('Passo:'))

for n in range(i,f,p):
    print(n)