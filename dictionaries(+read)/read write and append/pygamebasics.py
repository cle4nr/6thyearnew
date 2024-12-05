import pygame

pygame.init()

scr_width = 800
scr_height = 600

scr = pygame.display.set_mode((scr_width, scr_height))
player = pygame.Rect((300,300,50,50))

playing = True
while playing:
    scr.fill((255,255,255))
    pygame.draw.rect(scr,(255,0,0),player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
        
        
    
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    pygame.display.update()
pygame.quit()
    
    
