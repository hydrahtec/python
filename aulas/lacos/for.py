# lista = [2,6,9,5,3,8,6]
# palavra = 'Boson'

# for letra in palavra: 
#     print(letra)

# for numero in range(1,11):
#     print(numero)

# nome = input('Digite seu nome: ')

# for x in range(10):
#     print(f'{x+1} {nome}')

# range(Valor_inicial, valor_final, incremento)

# for x in range(20,2,-2):
#     print(x)

pedras = ('rubi', 'esmetaldo', 'quartzo', 'diamante')

for pedra in pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)