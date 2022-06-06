import pygame
pygame.mixer.init()

pygame.init()
pygame.mixer.music.load('/home/familiaomena/Documentos/MeusProjetos/Python_Curso_em_video/Mundo 01/exe021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
