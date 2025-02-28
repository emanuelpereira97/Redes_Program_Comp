import pygame #importando biblioteca pygame
from pygame.locals import* #submodolo que contem constantes e funções
from sys import exit #importando a função exit da biblioteca sys

pygame.init() #inicializa a biblioteca pygame

largura = 640 #largura da tela
altura = 480 #altura da tela

tela = pygame.display.set_mode((largura,altura)) #definições do objeto Tela
pygame.display.set_caption('O jogovo')

while True: #loop principal, o jogo roda aqui
    for event in pygame.event.get(): #esse loop verifica se algum evento ocorreu (clicou, teclou ...)
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update() #atualiza a tela a cada interação
