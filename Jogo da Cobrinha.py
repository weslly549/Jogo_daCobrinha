import pygame

#submódulo
# contem todas as funções para script de jogo
from pygame.locals import *

#função criada para fechar a janela
from sys import exit

# função que sorteia um valor em determinado intervalo.
from random import randint

#para iniciar as bibliotecas
pygame.init()

#musica de fundo
#deixando a musica de fundo menor
pygame.mixer.music.set_volume(0.1)
#definindo a musica de fundo 
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
#definindo a velocidade da reprodução da música
pygame.mixer.music.play(-1)

# som de colisão
# todos os arquivos que não sejam a música de fundo, tem que ser extensão wav
barulho_colisão = pygame.mixer.Sound('smw_coin.wav')



#criando janela inicial

largura = 640
altura = 480

#variaveis criadas para controlar o movimento do objeto na tela
#para fazer o objeto se mover no meio, define x como a largura/2
x_cobra = int(largura / 2)
y_cobra = int(altura /2)

# para fazer a cobtra se mover sempre
velocidade = 10
x_controle = velocidade
y_controle = 0


# valores para usar na random randint
# primeiro valor é inicial, e o segundo é o final
# os valores tem que ser menores que o tamanho da tela
x_maça = randint(40, 600)
y_maça = randint(50, 430)

#criando variável pontos
pontos = 0

#definindo texto na tela
#o True é para dizer se é negrito ou não
#o segundo True é para saber se o texto é iálico ou não
fonte = pygame.font.SysFont('arial', 40, True, True)


tela = pygame.display.set_mode((largura, altura))
#definindo nome da aba de tela do jogo
pygame.display.set_caption("jogo do weslly")
# como alterar a velocidade da atualização dos frames
relogio = pygame.time.Clock()

lista_cobra = []
# função para aumentar o tamanho da cobra

comprimento_inicial = 5

morreu = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY é uma lista com os valores de x e y
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

#função para reiniciar o jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_xobra, lista_cobra, lista_cabeca, x_maça, y_maça, morreu  
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura /2)
    lista_cobra = []
    lista_cabeca = []

    x_maça = randint(40, 600)
    y_maça = randint(50, 430)
    morreu = False
    

    


#loop para renderizar o jogo
while True:
    #relogio é a velocidade de atualização dos frames
    relogio.tick(25)
    #onde escolhe a cor
    tela.fill((255,255,255))

    
    mensagem = f'pontos: {pontos}'

    #definindo o formato e a cor da fonte
    texto_formatado = fonte.render(mensagem, True,(0,0,0))
    # for usado para detectar um comando feito pelo jogador
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            
        # definindo comando para mover o objeto
        #pass bloqueia um determinado comando
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        

    

    
    #desenhando retangulo sempre usado RGB
    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra,y_cobra,20,20))
    # x_azul e y_azul possuem os parâmetros de randint
    maça = pygame.draw.rect(tela,(255,0,0), (x_maça, y_maça,20,20))
    
    #define a ação de randint para o sistema mudar o retangulo azul quando
    #colidir com o retangulo vermelho
    
    if cobra.colliderect(maça):
        x_maça = randint(40, 600)
        y_maça = randint(50,430)

        #adicionando os pontos sempre que o vermelho colidir no azul
        pontos = pontos + 1
        #executando o som de colisão quando ocorre o choque entre os retangulos
        barulho_colisão.play()
        #fazer cobra ficar maior
        comprimento_inicial = comprimento_inicial + 1
        

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = "Game Over! Presisone a tecla R para jogar novamente"
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        Ret_texto = texto_formatado.get_rect()

        
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            Ret_texto.center = (largura // 2,altura // 2)            
            tela.blit(texto_formatado, (Ret_texto))       
            pygame.display.update()


    
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    

    aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado, (450,40))
    pygame.display.update()

            
# as informações quanto a localização dos ítens, usa-se o plano cartesiano
# maior itensidade da cor é 255
