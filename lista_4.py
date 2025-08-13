'''# 1° Questão
n=float(input('Digite uma nota: '))
while 0 <= n <= 10:
    n=float(input('Digite outra nota: '))
else:

    print('Inválido!!')
print()
#fimm


#2° Questão
usu=input('Nome de usuário: ')
sen=input('Senha: ')
while sen==usu:
    print('A senha deve ser diferente do seu nome de usuário!!!')
    usu=input('Nome de usuário: ')
    sen=input('Senha: ')   
else:
    print('Logim realizado com sucesso!')
print()
#fimmm


#3° Questão
nome=input('Nome: ')
while len(nome) <= 3 :
    print('Usuário deve conter mais de 3 caracteres!')
    nome=input('Nome: ')
    
idade=int(input('Idade: '))
teste= 0 < idade <= 150
while teste == False:
    print('Apenas entre 0 e 150!!!')
    idade=int(input('Idade: '))
    
salar=float(input('Salário: '))
while salar <=0:
    print('O salário deve ser maior que 0!!')
    salar=float(input('Salário: '))
    teste= 0 < idade <= 150
    
sex=input('Sexo: ')
while sexo != 'f' and sexo != 'm':
    print('Sexo inválido, apenas f ou m')
    sex=input('Sexo: ')

estad=input('Estado Civil: [s,c,v,d]')
while estad != 's' and estad != 'c' and estad != 'v' and estad != 'd':
    print('Estado civil incorreto!!')
    estad=input('Estado Civil: [s,c,v,d]')
print()



#4°Questão
pop_a=80000
pop_b=200000
tax_a=3/100
tax_b=1.5/100
anos=1
while pop_a < pop_b:
    pop_a = pop_a + (pop_a * tax_a)
    pop_b = pop_b + (pop_b * tax_b)
    anos= anos + 1
print('Leva', anos, 'anos')
print()


#5°Questão
pop_a = float(input('população 1: '))
pop_b = float(input('população 2: '))
tax_a = float(input('taxa 1: '))/100
tax_b = float(input('taxa 2: '))/100
anos = 1
if pop_a < pop_b:
     while pop_a < pop_b:
         pop_a = pop_a + (pop_a * tax_a)
         pop_b = pop_b + (pop_b * tax_b)
         anos = anos + 1
else:
     while pop_a > pop_b:
         pop_a = pop_a + (pop_a * tax_a)
         pop_b = pop_b + (pop_b * tax_b)
         anos = anos + 1
         print('Leva', anos, 'anos')
print()
#fimmm


#6°Questão
n=1
while n <=20:
    print(n)
    n=n+1
nn=1
while nn <=20:
    print(nn, end=(' '))
    nn=nn+1
print()
#fimm


#7°Questão
cont=0
aux=0
while cont < 5:
    n = int(input('Digite um número: '))
    if n >= aux:
        aux = n
    cont = cont + 1
print('maior: ',aux)
print()
#fimm


#8°Questão

cont=0
soma=0
while cont < 5:
    n = int(input('Digite um número: '))
    soma= soma + n
    cont = cont + 1
media=soma/5
print('Soma: ',soma)
print('Media: ',media)
print()
#fimm



#9°Questão
n=1
while n <=50:
    print(n, end=' ')
    n = n+2
print()
#fimmm
'''

#10°Questão
n1=int(input('Inicio: '))+1
n2=int(input('Fim: '))-1
while n1 <= n2:
    print(n1)
    n1=n1+1


























































































