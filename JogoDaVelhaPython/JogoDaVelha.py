import os

posicao = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 
           5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
def desenhaJogo(posicao1,posicao2,posicao3,posicao4,posicao5,posicao6,posicao7,posicao8,posicao9):
    print('      |     |      ')
    print('   {0}  |  {1}  |  {2} '.format(posicao1,posicao2,posicao3))
    print('______|_____|______')
    print('      |     |      ')
    print('   {0}  |  {1}  |  {2} '.format(posicao4,posicao5,posicao6))
    print('______|_____|______')
    print('      |     |      ')
    print('   {0}  |  {1}  |  {2} '.format(posicao7,posicao8,posicao9))
    print('      |     |      ')

i = 0
while (i < 9):
    desenhaJogo(posicao[1],posicao[2],posicao[3],
                posicao[4],posicao[5],posicao[6],
                posicao[7],posicao[8],posicao[9])
    escolha = int(input('Escolha a posição: '))
    posicao[escolha] = input('Faça a sua jogada: ')
    while posicao[escolha] != 'X' and posicao[escolha] != 'O':
        posicao[escolha] = input('Erro! Use apenas "X" ou "O"')
            
    os.system('clear') #or None
    i += 1
    if i == 9:
        print('Empate')
