nome = str(input('Digite um nome: '))

n = nome.split()

print('Primeiro nome: {0} ; Último nome: {1}'.format(n[0],n[len(n)-1]))