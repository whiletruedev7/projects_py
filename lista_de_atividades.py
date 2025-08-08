#1° questão
print('---Controle de Gastos Mensais---')
alimentacao=float(input('Qual foi seu gasto com alimentação este mês?'))
transporte=float(input('Qual foi seu gasto com transporte esse mês?'))
lazer=float(input('Qual foi seu gasto com lazer esse mês?'))
print()
print('---Resumo dos Gastos---')
resum=(alimentacao+transporte+lazer)
print('Alimentação:R$',alimentacao)
print('Transporte:R$',transporte)
print('Lazer:R$',lazer)
print('Total de Gastos:',resum)
print()
#questão gasto mensal

#2° Questão 'conversor de temperatura'
print('---Conversor de Temperatura---')
print()
far=float(input('Digite a temperatura em Fahrenheit:'))
cal=((far-32)*5/9)
print('A temperatura em Celsius é:',cal)
print()
#questão temperatura

#3° Questão 'Área do Retângulo
print('---Calculadora de Área de terreno---')
print()
com=float(input('Digite o comprimento do terreno:'))
larg=float(input('Digite a largura do terreno:'))
print()
resul=(com*larg)
print('A área do terreno é:',resul,'metros quadrados.')
print()
#questão retângulo

#4° Questão 'Médias de Notas
print('---Calculadora de Média---')
print()
n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
print()
cal=((n1+n2)/2)
print('A média das notas é:',cal)
print()
#questão média

#5° Questão 'Calculadora de Descontos de Produto
print('---Calculadora de Desconto---')
print()
orig=float(input('Digite o preço original do prduto:'))
desc=float(input('Digite a porcentagem de desconto:'))
print()
cal=(orig*desc/100)
print('Valor do Desconto',cal)
print('Preço final com desconto:R$',orig-cal)
print()
#calculo de desconto

#6° Questão 'Divisor de Contas de Restaurante'
print('---Divisor de Contas de Restaurante---')
print()
tot=float(input('Qual o valor total da conta?'))
quant=float(input('Quantas pessoas vão dividir a conta?'))
print()
cal=(tot/quant)
print('Cada pessoa deve pagar:R$',cal)
print()
#quastão do restaurante

#7° Questão 'Calculadora de Idade em Dias'
print('---Calculadora de Idade em Dias---')
print()
ida=int(input('Quantos anos você tem?'))
print()
cal=(ida*365)
print('Você já viveu aproximadamente',cal)
print()
#quatão da idade

#8° Questão 'Inversão de Valores'
print('---Inversão de Valores---')
print()
v1=int(input('Digite o primeiro valor:'))
v2=int(input('Digite o segundo valor:'))
print()
print('Valores antes da troca:')
print('Primeiro valor:',v1)
print('Segundo valor:',v2)
print()
print('Valores depois da troca:')
print('Primeiro valor:',v2)
print('Segundo valor:',v1)
print()
#questão inversão

#Atividade extra: 'Calculadora de Custos de Viagem de Carro'
print('---Calculadora de Cutos de Viage de Carro---')
print()
print('Por favor, insira os dados da sua viagem:')
print()
dis=float(input('Qual a distância total da viagem em km?'))
cons=float(input('Qual o consumo médio do seu carro(km/l)?'))
price=float(input('Qual o preço médio do litro da gasolina(R$)?'))
pess=float(input('Quantas pessoas irão na viagem(incluindo você)?'))
print()
print('---Resumo do Custo da Viagem---')
print()
print('Detalhe da Viagem:')
print('-Distância Total:',dis,'km')
print('-Consumo do Carro:',cons,'km/L')
print('-Preço da Gasolina:',price,'/L')
print('-Pessoas na Viagem:',pess)
print()
#calculos
calc1=(dis/cons)
calc2=(calc1*price)
calc3=(calc2/pess)
print('Cálculos:')
print('-Volume de Gasolina Necessário:',calc1,'litros')
print('-Custo Total da Gasolina:R$',calc2)
print('-Custo por Pessoa(Gasolina):R$',calc3)
print()
print('Boa Viagem!')
