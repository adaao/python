import pygame

arquivo_mp3 = '7-rings-lyrics.mp3'
pygame.mixer.init()
pygame.mixer.music.load(arquivo_mp3)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(100)
input()
pygame.event.wait()
