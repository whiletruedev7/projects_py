altura= float(input('Qual a sua altura?'))
peso=float(input('qual seu peso?'))
print()
                 
imc=((peso/altura**2))*10000

print(imc)          

print('-----vê se tá gordo:-----')
print(' <18,5: anorexia\n','>18,5 até 24,9: massa man\n','>=25 até 29,9: tá engoradando, man\n','De 30,0 a 34,9: gordim\n','De 35,0 a 39,9: Gordim level 2\n','>=40,0:gordaço, man...')
