secret=7
palpite=0
while secret!=palpite:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == secret:
        print(' acertou!')
        
    else:
        print('Errou. Tente novamente.')

