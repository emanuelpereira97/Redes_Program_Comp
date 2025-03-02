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
    pygame.draw.rect(tela,(255,0,125), (320,240,30,50)) #desenha retangulo p(onde,cor,(posição xy, Largura e altura))
    pygame.draw.circle(tela,(255,255,255), (160,120), 35) #desenha um circulo, paramentros semelhantes, troca L*H por raio
    pygame.draw.line(tela,(100,120,140),(500,0),(0,400),5) #desenha linha, ponto inicial, ponto final e espessura
    pygame.display.update() #atualiza a tela a cada interação
