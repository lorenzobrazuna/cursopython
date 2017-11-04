lado1 = int(input('Digite o lado 1 do possível triangulo: '))
lado2 = int(input('Digite o lado 2 do possível triangulo: '))
lado3 = int(input('Digite o lado 3 do possível triangulo: '))

if (abs(lado2-lado3)<lado1<(lado2+lado3) and abs(lado1-lado3)<lado2<(lado1+lado3) and abs(lado1-lado2)<lado3<(lado1+lado2)):
    print('O Triangulo poderá ser formado!!')
else:
    print('O Triangulo não poderá ser formado!')