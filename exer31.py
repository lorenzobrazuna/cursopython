dist = int(input('Digite a distancia em Km da viagem: '))

if dist <= 200:

    valor = dist*0.5
    print('O valor da viagem será: {:.2f} reais'.format(valor))
else:
    valor = dist*0.45
    print('O valor da viagem será: {:.2f} reais'.format(valor))
