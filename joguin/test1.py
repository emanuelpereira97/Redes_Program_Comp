import pygame #importando biblioteca pygame
from pygame.locals import* #submodolo que contem constantes e funções
from sys import exit #importando a função exit da biblioteca sys

pygame.init() #inicializa a biblioteca pygame

clock = pygame.time.Clock()#FPS

#Configurações da tela
pygame.display.set_caption('JogOvo')#Titulo do jogo, escreve da barra superior
largura_tela = 640 #largura da tela
altura_tela = 480 #altura da tela
tela = pygame.display.set_mode((largura_tela,altura_tela)) #definições do objeto Tela

#cores
branco = (255,255,255)
preto = (0,0,0)

#Configurações das Nuvens laterais pequenas
y_nuvem = 0
largura_nuvens_1 = 150
altura_nuvens_1 = 45
largura_nuvens_laterais = 60
altura_nuvens_laterais = 58

#Nuvem lateral grande


#Nuvem central
largura_nuvem_central_1 = 150
largura_nuvem_central_2 = 100
posicao_x_nuvem_central_1 = (largura_tela/2)-(largura_nuvem_central_1/2)
posicao_x_nuvem_central_2 = (largura_tela/2)-(largura_nuvem_central_2/2)

#Configurações do Ovo
largura_ovo = 30
altura_ovo = 45
#centraliza a posição do Ovo
posicao_x_ovo = (largura_tela/2)-(largura_ovo/2)
posicao_y_ovo = (altura_tela/2)-(altura_ovo/2)

while True: #loop principal, o jogo roda aqui

    base_ultima_nuvem = 840-y_nuvem
    clock.tick(60)
    tela.fill((preto))
    for event in pygame.event.get(): #loop principal verifica se algum evento ocorreu (clicou, teclou ...)
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Moviumento do Ovo em X (precionar)---------------       
    if pygame.key.get_pressed()[K_LEFT]:
        posicao_x_ovo -= 3
    elif pygame.key.get_pressed()[K_RIGHT]:
        posicao_x_ovo += 3
    elif pygame.key.get_pressed()[K_UP]:
        posicao_y_ovo -= 3
    elif pygame.key.get_pressed()[K_DOWN]:
        posicao_y_ovo += 3
    #-------------------------------------------------
    
    #Compondo nuvem da esquerda
    nuvem_esq_1 = pygame.draw.ellipse(tela,branco, (14,(435-y_nuvem),largura_nuvens_1,altura_nuvens_1))
    nuvem_esq_2 = pygame.draw.ellipse(tela,branco, (4,(409-y_nuvem),largura_nuvens_laterais,altura_nuvens_laterais))
    nuvem_esq_3 = pygame.draw.ellipse(tela,branco, (50,(420-y_nuvem),largura_nuvens_laterais,altura_nuvens_laterais))

    #Compondo nuvem da direita
    nuvem_dir_1 = pygame.draw.ellipse(tela,branco, (476,(435-y_nuvem),largura_nuvens_1,altura_nuvens_1))
    nuvem_dir_2 = pygame.draw.ellipse(tela,branco, (466,(409-y_nuvem),largura_nuvens_laterais,altura_nuvens_laterais))
    nuvem_dir_3 =pygame.draw.ellipse(tela,branco, (520,(420-y_nuvem),largura_nuvens_laterais,altura_nuvens_laterais))

    #Compondo nuvem central
    nuvem_central_1 = pygame.draw.ellipse(tela,branco, ((posicao_x_nuvem_central_1),(560-y_nuvem),largura_nuvem_central_1,45))
    nuvem_central_2 = pygame.draw.ellipse(tela,branco, ((posicao_x_nuvem_central_2),(534-y_nuvem),largura_nuvem_central_2,58))
    
    #Compondo nuvem grande da esquerda
    nuvem_g_esq_1 = pygame.draw.ellipse(tela,branco, (84,(700-y_nuvem),106,altura_nuvens_1))
    nuvem_g_esq_2 = pygame.draw.ellipse(tela,branco, (4,(704-y_nuvem),110,altura_nuvens_laterais))
    nuvem_g_esq_3 = pygame.draw.ellipse(tela,branco, (24,(715-y_nuvem),290,altura_nuvens_laterais))

    #Compondo nuvem grande da direita
    nuvem_g_dir_1 = pygame.draw.ellipse(tela,branco, (380,(825-y_nuvem),106,altura_nuvens_1))
    nuvem_g_dir_2 = pygame.draw.ellipse(tela,branco, (300,(815-y_nuvem),110,altura_nuvens_laterais))
    nuvem_g_dir_3 = pygame.draw.ellipse(tela,branco, (340,(base_ultima_nuvem),290,altura_nuvens_laterais))

    ovo = pygame.draw.ellipse(tela,branco, (posicao_x_ovo,posicao_y_ovo,largura_ovo,altura_ovo))

    #Junta as partes das nuvens em uma lista
    nuvens_lista_colisao = [nuvem_esq_1,nuvem_esq_2,nuvem_esq_3,nuvem_dir_1,nuvem_dir_2,nuvem_dir_3,nuvem_central_1,nuvem_central_2]

    #Faz as nuvens voltarem a base da tela quando aringirem o limte superior
    if base_ultima_nuvem <= -100:
        y_nuvem = 0
    #----------------------------------------------------------------------

    #Mantem o Ovo dentro do enquadro da tela 
    if posicao_x_ovo >= 610:
        posicao_x_ovo = 610
    elif posicao_x_ovo <= 0:
        posicao_x_ovo = 0
    #---------------------------------------------------------------------

    #Movimenta a nuvem verticalmente para cima a cada loop
    y_nuvem += 1
    
    #verifica se o Ovo colodiu com algum objeto da lista
    if ovo.collidelistall(nuvens_lista_colisao):
        print("Colidiu com nuvem")

    pygame.display.update() #atualiza a tela a cada interação