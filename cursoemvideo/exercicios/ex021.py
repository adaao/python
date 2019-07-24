'''
21 - Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
'''

import pygame
import os

arquivo_mp3 = '7-rings-lyrics.mp3'
diretorio_do_arquivo_mp3 = 'C:/Users/adaao/Documents/dev/python/cursoEmVideo/python/cursoemvideo/'

if os.path.exists(diretorio_do_arquivo_mp3 + arquivo_mp3):
    pygame.mixer.init()
    size = width, height = 300, 100
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load(diretorio_do_arquivo_mp3 + arquivo_mp3)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(100)
    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('Arquivo não encontrado')

