numero = int(input('Digite o Número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("A Unidade do numero {} será - \n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}".format(numero,unidade,dezena,centena,milhar))