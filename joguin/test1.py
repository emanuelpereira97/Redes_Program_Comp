import pygame #importando biblioteca pygame
from pygame.locals import* #submodolo que contem constantes e funções
from sys import exit #importando a função exit da biblioteca sys

pygame.init() #inicializa a biblioteca pygame

pygame.display.set_caption('JogOvo')

largura = 640 #largura da tela
altura = 480 #altura da tela
tela = pygame.display.set_mode((largura,altura)) #definições do objeto Tela

branco = (255,255,255)
preto = (0,0,0)


x = 0
y = 0

while True: #loop principal, o jogo roda aqui
    tela.fill((preto))
    for event in pygame.event.get(): #loop principal verifica se algum evento ocorreu (clicou, teclou ...)
        if event.type == QUIT:
            pygame.quit()
            exit()
    nuvem_esq = [pygame.draw.ellipse(tela,branco, ((14-x),(435-y),150,45)), pygame.draw.ellipse(tela,branco, ((4-x),(409-y),60,58)), pygame.draw.ellipse(tela,branco, ((50-x),(420-y),60,40))]
    nuvem_dir = [pygame.draw.ellipse(tela,branco, ((476-x),(435-y),150,45)), pygame.draw.ellipse(tela,branco, ((576-x),(409-y),60,58)), pygame.draw.ellipse(tela,branco, ((520-x),(420-y),60,40))]
    ovo = pygame.draw.ellipse(tela,branco, (300,200,30,45)) #desenha um circulo, paramentros semelhantes, troca L*H por raio
    if y >= altura:
        y = 0
    y += 1
    
    pygame.display.update() #atualiza a tela a cada interação
