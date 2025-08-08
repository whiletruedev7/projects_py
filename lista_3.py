
#Questão 1
num=int(input('Digite um número:'))
num2=int(input('Digite outro número:'))
print()
if num>num2:
    print(num,'é o maior número')
else:
    if num==num2:
      print('Os números digitados foram iguais!')
    else:
     print(num2,'é o maior número')
print()
#fim



#Questão 2
num=int(input('Digite um número:'))
if num <0:
    print(num, 'É negativo')
else:
      if num==0:
       print(num,'É 0, se não gostou questiona os matemáticos que se mataram pra chegar nessa   conclusão!!')
      else:  
       print(num, 'É positivo')
print()
#fim



#Questão 3
let=input('Dá uma letra pá nois')
if let=='F':
    print('Feminino')
else:    
    if let=='M':
     print('Masculino')
    else:
     print('Sexo inválido')
print()
#fim



#Questão 4
let1=input('Digite uma letra')
print()
if let1=='a':
    print('A letra informada é uma vogal')
else:
    if let1=='e':
        print('A letra informada é uma vogal')
    else:
        if let1=='i':
            print('A letra informada é uma vogal')
        else:
            if let1=='o':
                print('A letra informada é uma vogal')
            else:
                if let1=='u':
                    print('A letra informada é uma vogal')
                else:
                    print('A letra informada é uma consoante')
print()                    
#fim



#Questão 5
n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite asegunda nota:'))
print()
calc=((n1+n2)/2)
if calc==7.0:
    print('Aprovado')
else:
    if calc==8.0:
     print('Aprovado')
    else:
        if calc==9.0:
            print('Aprovado')
        else:
            if calc==10.0:
                print('Aprovado com Distinção')
            else:
             print('Reprovado')
print()
#fim

 

#Questão 6
nu1=int(input('Digite um número:'))
nu2=int(input('Digite um número:'))
nu3=int(input('Digite um número:'))
print()
maior = nu1
if nu3 > maior:
    print(nu3,'É o maior número')
elif nu2 > maior:
    print(nu2,'É o maior número')
else:
    print(maior,'É o maior número')
print()
#fim


#Questão 7
nu1=int(input('Digite um número:'))
nu2=int(input('Digite um número:'))
nu3=int(input('Digite um número:'))    
print()
maior = nu1
if nu3 > maior:
    print(nu3,'É o maior número')
elif nu2 > maior:
    print(nu2,'É o maior número')
else:
    print(maior,'É o maior número')
menor = nu1
if nu3 < maior:
    print(nu3,'É o menor número')
elif nu2 < maior:
    print(nu2,'É o menor número')
else:
    print(maior,'É o menor número')
print()
#fim

#Questão 8
p1=float(input('Valor do produto:'))
p2=float(input('Valor do produto:'))
p3=float(input('Valor do produto:'))    
print()
menor = p1
if p3 < menor:
    print(p3,'É o mais barato')
elif p2 < menor:
    print(p2,'É o mais barato')
else:
    print(menor,'É o mais barato')
print()
#fim


#Questão 9
nu1=int(input('Digite um número:'))
nu2=int(input('Digite um número:'))
nu3=int(input('Digite um número:'))    
print()
if nu1 >= nu2:
    if nu1 >= nu3:
        print(nu1)
        if nu2 >= nu3:
            print(nu2)
            print(nu3)¨$
        else:
            print(nu3)
            print(nu2)
    else:
        print(nu3)
        print(nu1)
        print(nu2)
else:
    if nu2 >= nu3:
        print(nu2)
        if nu1 >= nu3:
            print(nu1)
            print(nu3)
        else:
            print(nu3)
            print(nu1)
    else:
        print(nu3)
        print(nu2)
        print(nu1)

#NÃO CONCLUIDA!!!!!!!!!!



#fim

#Questão 10
let=input('Digite a inicial do seu turno:')
print()
if let=='M':
    print('Bom Dia!')
else:
    if let=='V':
        print('Boa Tarde!')
    else:
        if let=='N':
            print('Boa Noite')
        else:
            print('Turno Invalido!')
print()
#fimm


#Questão 11
salario_atual = float(input('Digite o salário atual do colaborador:'))
print()

if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

print('Salário antes do reajuste:',salario_atual)
print('Percentual de aumento aplicado:',percentual)
print('Valor do aumento:',valor_aumento)
print('Salário após o aumento:',novo_salario)
print()
#fimm

