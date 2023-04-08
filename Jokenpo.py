
import random # Importar a biblioteca RANDOM

def jokenpo():
    while True: # Laço infinito
        jogada = input("Escolha entre PEDRA, PAPEL OU TESOURA: ").upper() # Solicita ao usuário a jogada
        while jogada not in movimentos:
            jogada = input("Movimento inválido. Escolha entre PEDRA, PAPEL OU TESOURA: ").upper()
        computador = random.choice(movimentos) # Escolhe uma jogada aleatória da lista 'movimentos'
        print(f'Você escolheu {jogada} e o computador escolheu {computador}\n') # infoma quais jogadas escolhidas
        return jogada, computador

    #Verifica as jogadas e informa o resultado
def resultado(jogada, computador):
    while jogada == computador:
        print('Eitaa... Deu empate. Tente novamente!\n')
        jogada, computador = jokenpo()

    if (jogada == 'PEDRA' and computador =='TESOURA') or (jogada == 'PAPEL' and computador =='PEDRA') or (jogada == 'TESOURA' and computador =='PAPEL'):
        return f'{jogada} ganha para {computador}\nParabéns, você venceu!!'
            
    else:
        return f'{jogada} perde para {computador}.\nAhhh... Você perdeu.'
            
movimentos = ['PEDRA', 'PAPEL', 'TESOURA'] # Lista com os movimentos

print('''Bem vindo(a) ao jogo Jokenpô!

##################################################
#                    REGRAS                      #
##################################################
#                                                #
#  1. Pedra ganha de Tesoura e perde para Papel  #
#  2. Tesoura ganha de Papel e perde para Pedra  #
#  3. Papel ganha de Pedra e perde para Tesoura  #
#                                                #
##################################################

Vamos começar?!
''')

jogada, computador = jokenpo()
print(resultado(jogada, computador))
