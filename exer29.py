velo = int(input('Digite a velocidade do carro: '))

if velo > 80:
    multa = 7 + (velo-80)
    print('O carro foi multado em {}'.format(multa))

else:
    print('O carro não foi ')