#Questão 1
print('---Calculadora de Custos de Deslocamento---')
print()
dis=float(input('Qual a sua distância diária de deslocamento?'))
dias=float(input('Quantos dias úteis você se desloca no mês?'))
price=float(input('Qual o preço de uma passagem de ônibus?'))
med=float(input('Qual o preço médio de gasolina?'))
cons=float(input('Qual o consumo do seu carro?'))
bike=float(input('Qual o custo mensal de manutenção da bicicleta?'))
print()
print('---Resumo de Custos Mensais---')
print()
#calculo onibus
calc1=((price*2)*dias)
#calculo carro
calc2=(dis*dias)
calc3=(calc2/cons)
calc4=(calc3*med)
##
print('Custo de Ônibus:R$',calc1)
print('Custo de carro:R$',calc4)
print('Custo de Bicicleta:R$',bike)
print()
#fim da questão 1

#Questão 2
print('---Simulador de Contas Residenciais---')
print()
cons1=float(input('Digite o consumo de água do mês em m³:'))
tar1=float(input('Digite a tarifa de água por m³:'))
cons2=float(input('Digite o consumo de energia do mês em kWh:'))
tar2=float(input('Sigite a tarifa de energia porkWh:'))
print()
#calculos
calc1=(cons1*tar1)
calc2=(cons2*tar2)
calc3=(calc1+calc2)
##
print('---Relatório de Consumo---')
print()
print('Custo de Água:',calc1)
print('Custo da Energia:',calc2)
print()
print('Custo Total(Água+Energia):R$',calc3)
print()
#fim da questao 2

#Questão 3
print('---Calculadora de Calorias---')
print()
peso=float(input('Qual o seu peso em kg?'))
temp1=float(input('Quantos minutos você caminhou?'))
temp2=float(input('Quantos minutos você correu?'))
temp3=float(input('Quantos minutos você pedalou?'))
print()
#calculos
calc1=(peso*temp1*0.05)
calc2=(peso*temp2*0.1)
calc3=(peso*temp3*0.08)
tt=(calc1+calc2+calc3)
##
print('---Resumo de Gasto Calórico---')
print()
print('Caminhada:',calc1,'kcal')
print('Corrida:',calc2,'kcal')
print('Ciclismo:',calc3,'kcal')
print()
print('Total de Calorias Queimadas:',tt,'kcal')
print()
#fim da questao 3



#Questão 5
print('---Ajustador de Receitas---')
print()
orig=float(input('A receita original rende quantas porções?'))
faz=float(input('Quantas porções você quer fazer?'))
print()
#variaveis
ajust=faz/orig
far=400
açu=300
ovos=3
print('[Receita Original (para 8 porções)]')
print('Farinha:',far)
print('Açucar:',açu)
print('Ovos:',ovos)
print()
print('---Receita Ajustada (para 12 porções)---')
print('Farinha:',far*ajust)
print('Açucar:',açu*ajust)
print('Ovos:',ovos*ajust)
print()
#fim da questao 5

#Questão 6
print('---Calculadora de Salário e Horas Extras---')
print()
sal=float(input('Qual o salário bruto do funcionário?'))
extra=float(input('Quantas horas extras ele trabalhou este mês?'))
norm=13.64
vextra=20.45
print()
print('---Resumo do Salário---')
print()
print('Salário Bruto Mensal:R$',sal)
print('Valor da Hora Normal:R$',norm)
print('Valor da Hora Extra:R$',vextra)
print()
print('Total a Receber por Horas Extras:R$',extra*vextra)
print('Salário Final do Mês:R$',(extra*vextra)+sal)
print()
#fim da questao 6

#Questão 7
print('---Gerenciador de Custos de Combustível(Carro e Moto)---')
print()
price=float(input('Qual o preço médio da gasolina(R$)?')
dist=float(input('Qual a distância total que você percorre por mês em km?'))
dia1=float(input('Em quantos dias no mês você usa o carro?'))
dia2=float(input('Em quantos dias no mês você usa a moto?'))
print()
print('---Detalhes e Cálculos---')
print()
print('Distância Média Diária:',dist/(dia1+dia2))
print()
print('Informações do Carro:')
cons1=float(input('Qual o consumo do seu carro (km/L)?'))
