from random import randint

num = randint(0,5)
print(num)
numuser = int(input('Qual o número que o computador pensou? '))

if numuser == num:
    print('Parabéns! Você acertou!')
else:
    print('Você errou.')


