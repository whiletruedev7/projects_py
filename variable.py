from datetime import datetime
agora=datetime.now()
var= 'valor disponivel:' 
saldo_da_conta=1000.0
nome_cliente='John Doe'
usuario='cliente:'
ex='     extrato:'
px='pix recebido:300.0'
dk=300.0
print(usuario,nome_cliente)
print(var,saldo_da_conta)
print(ex)
print('-----------------------')
print(px)
print(var,saldo_da_conta+dk)
print("Horário:",agora.strftime("%H:%M:%S"))
