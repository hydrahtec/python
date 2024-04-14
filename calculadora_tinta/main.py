largura = float(input('Qual a largura do comodo? '))
altura = 2.9
profundidade = float(input('Qual a profundidade do comodo? '))

area_paredes: float = 2 * (largura + profundidade) * altura

print('A area das paredes é: ', area_paredes, 'M²')

area_teto: float = largura * altura

print('A area do teto é: ', area_teto, 'M²')

print('A litragem de tint necessaria é: ',
      (area_paredes + area_teto) / 10, 'M²'
      )