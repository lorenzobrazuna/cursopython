num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))
num3 = int(input('Digite o numero 3: '))

if (num1 > num2):
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

if maior < num3:
    maior = num3
elif menor > num3:
    menor = num3

print('O numero {} é o maior, e o numero {} é o menor'.format(maior,menor))