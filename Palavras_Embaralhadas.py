import random

def sortear_palavra():
    palavras = open('palavras.txt', 'r', encoding='utf-8').readlines() # Abrir o arquivo txt e atribuir em forma de lista na variável
    palavras = list(map(str.strip, palavras)) # Mapear a lista e retirar os espaços (antes e depois) e quebras de linhas de cada palavra

    palavra_aleatoria = random.choice(palavras).upper()  # Escolher uma palavra aleatória da lista
    palavra_embaralhada = list(palavra_aleatoria) # Transformar a string em lista de caracteres
    random.shuffle(palavra_embaralhada) # Embaralhar as letras
    palavra_embaralhada = (''.join(palavra_embaralhada)) # Transformar a lista das letras em uma string em letras maiúsculas

    return palavra_aleatoria, palavra_embaralhada


def jogar(palavra_aleatoria):
    tentativas = 0
    for chance in range(7): # Laço de repetição para 7x
        if tentativas == 6: #Se o número de tentativas erradas for igual a 6, entrar no if e encerrar.
            print(f'Ahhh... Você perdeu! A palavra correta era: {palavra_aleatoria}')
            break

        tentativa = input(f'{chance + 1}ª chance: ').upper()

        if tentativa != palavra_aleatoria: # Se a palavra digitada for diferente a palavra escolhida, entrar no if e adicionar 1 na variavel de tentativas
            if tentativas != 5: # Se for a última tentativa, não informar 'Tente novamente!'
                print('Tente novamente!')
            tentativas += 1

        else: # Se a palavra digitada for igual a palavra escolhida, entrar no if e encerar.
            print('Parabéns! Você acertou!\n')
            break

    
palavra_aleatoria, palavra_embaralhada = sortear_palavra()

print(f'''Bem vindo ao jogo da Palavra Embaralhada!
Você tem 6 chances para acertar a palavra escolhida. Vamos lá?!

A palavra escolhida é: {palavra_embaralhada}
''')

jogar(palavra_aleatoria)

