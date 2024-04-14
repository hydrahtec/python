from calculadora_mod import Calculadora
calc = Calculadora()

largura = float(input('Qual a largura do comodo? '))
altura = 2.9
profundidade = float(input('Qual a profundidade do comodo? '))

#calc.area_parede = 2 * (largura + profundidade) * altura

print('A area das paredes é: ', 
      calc.calcular_area_paredes(largura, profundidade, altura), 'M²')

#calc.area_teto = largura * altura

print('A area do teto é: ', 
      calc.calcular_area_teto(largura, profundidade), 'M²')

print('A litragem de tint necessaria é: ',
      calc.calcular_litragem_necessaria(), 'M²'
      )

# aula 7