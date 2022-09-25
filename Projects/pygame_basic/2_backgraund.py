import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('나도게임')

#배경이미지 불러오기
background = pygame.image.load('C:/Users/jdsmy/OneDrive/Documents/코딩DB/DB/python/projects/pygame_basic/background.png')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # screen.fill((0, 0, 255))
    screen.blit(background, (0,0)) #배경그리기

    pygame.display.update() #게임화면 다시 그리기

pygame.quit()