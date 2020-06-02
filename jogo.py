data=dict()
import random
from json import load
import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1)
while(pygame.mixer.music.get_busy()):
    for c in range(4):
        lista = list()
        for b in range(1, 11):
            for a in range(1, 10):
                if c == 0: #Soma
                    lista.append([f'{b}+', a, b+a])
                elif c == 1:#Subtração
                    lista.append([f'{a+b}-', b, a])
                elif c == 2: #Multiplicação
                    lista.append([f'{b}*', a, b*a])
                elif c == 3:# Divisão
                    lista.append([f'{a*b}/', b, a])
        if c == 0:#Soma
            data['S'] = lista.copy()
        elif c == 1:#Subtração
            data['Su'] = lista.copy()
        elif c == 2: #Multiplicação
            data['M'] = lista.copy()
        elif c == 3:# Divisão
            data['D'] = lista.copy()
    import json
    with open("dados.json", 'w') as f:
        json.dump(data, f)
    arquivo = open('dados.json')
    data = load(arquivo)
    arquivo.close()
    def jogo(caminho):
        for num in range(0 , len(caminho)-1):
            while True:
                try:
                    p=int(input(f"{caminho[num][0]}{caminho[num][1]} ="))
                    if p == caminho[num][2]:
                        print('Acertou!!!')
                        break
                    else:
                        print('errou!!')
                except:
                    pass
    print('Bem vindo à Tabugame!')
    nome=str(input('Digite o seu nome:'))
    print(f'Olá, {nome}! Bem, na sua primeira fase, você começará com a adição!')
    jogo(data['S'])
    print(f'Muito bem, {nome}! Agora começa a segunda fase, Subtração!')
    jogo(data['Su'])
    print(f'Sem mais delongas, a terceira fase, multiplicação!')
    jogo(data['M'])
    print(f'Muito bem, {nome}! Agora começa a quarta fase, multiplicação!')
    jogo(data['D'])
# Fases: Soma, Subtração, Multiplicação e Divisão