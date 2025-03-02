import pygame #importando biblioteca pygame
from pygame.locals import* #submodolo que contem constantes e funções
from sys import exit #importando a função exit da biblioteca sys

pygame.init() #inicializa a biblioteca pygame

pygame.display.set_caption('O jogovo')

largura = 640 #largura da tela
altura = 480 #altura da tela
tela = pygame.display.set_mode((largura,altura)) #definições do objeto Tela

branco = (255,255,255)
nuvem_esq = [pygame.draw.ellipse(tela,branco, (10,200,150,45)), pygame.draw.ellipse(tela,branco, (3,175,60,58)), pygame.draw.ellipse(tela,branco, (50,185,60,40))]
nuvem_dir = [pygame.draw.ellipse(tela,branco, (476,200,150,45)), pygame.draw.ellipse(tela,branco, (576,175,60,58)), pygame.draw.ellipse(tela,branco, (520,185,60,40))]
ovo = pygame.draw.ellipse(tela,branco, (300,200,30,45)) #desenha um circulo, paramentros semelhantes, troca L*H por raio

x = 0
y = 0

while True: #loop principal, o jogo roda aqui
    for event in pygame.event.get(): #loop principal verifica se algum evento ocorreu (clicou, teclou ...)
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    pygame.display.update() #atualiza a tela a cada interação
