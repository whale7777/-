from re import X
import pygame
import os
from tkinter import *
import random
import time as t

aaa = random.randint(1,100)




pygame.init()

보석먹음 = 0

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

path = os.getcwd()
bg_path = os.path.join(path, "background.png")
character_path = os.path.join(path, "character.png")
character_2_path = os.path.join(path, "character_2.png")
exit_path = os.path.join(path, "exit.png")
enemy_path = os.path.join(path, "enemy.png")
wall_path = os.path.join(path, "wall.png")
wall_path_2 = os.path.join(path, "wall.png")
Sulwin_path = os.path.join(path, "SulWin.png")
player_win_path = os.path.join(path, "playerwin.png")
Mu_path = os.path.join(path, "Mu.png")

pygame.display.set_caption("술래잡기")

background = pygame.image.load(bg_path)

    
    
    

set_wall1_xpos = 300
set_wall2_xpos = 700
set_wall1_ypos = 0
set_wall2_ypos = 300
    


def setting(path,xpos,ypos):
    name = pygame.image.load(path)
    name_size = name.get_rect().size 
    name_width = name_size[0]
    name_height = name_size[1]
    name_x_pos = xpos
    name_y_pos = ypos

    return name,name_size,name_width,name_height,name_x_pos, name_y_pos

c,c_size,c_width,c_height,c_xpos,c_ypos = setting(character_path,0,0)
c_2,c_size_2,c_width_2,c_height_2,c_xpos_2,c_ypos_2 = setting(character_2_path,920 , 520)
e,e_size,e_width,e_height,e_xpos,e_ypos = setting(enemy_path,465,265)
ex,ex_size,ex_width,ex_height,ex_xpos,ex_ypos = setting(exit_path,920,0)
w,w_size,w_width,w_height,w_xpos,w_ypos = setting(wall_path,set_wall1_xpos,set_wall1_ypos)
w_2,w_size_2,w_width_2,w_height_2,w_xpos_2,w_ypos_2 = setting(wall_path_2,set_wall2_xpos , set_wall2_ypos)
Mu = pygame.image.load(Mu_path)
player_win = pygame.image.load(player_win_path)
Sulwin = pygame.image.load(Sulwin_path)

to_x = 0
to_y = 0

to_x_2 = 0
to_y_2 = 0

clock = pygame.time.Clock()

player_speed = 0.95
speed = 0.7

game_font = pygame.font.Font(None, 40)

total_time = 120

start_ticks = pygame.time.get_ticks()

충돌함 = 0
보석먹음 = 0



running = True

winning = 0




while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                to_x += player_speed
            elif event.key == pygame.K_UP:
                to_y -= player_speed
            elif event.key == pygame.K_DOWN:
                to_y += player_speed

            if event.key == pygame.K_a:
                to_x_2 -= speed
            elif event.key == pygame.K_d:
                to_x_2 += speed
            elif event.key == pygame.K_w:
                to_y_2 -= speed
            elif event.key == pygame.K_s:
                to_y_2 += speed

    
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                to_x_2 = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y_2 = 0

    
            

    c_xpos += to_x
    c_ypos += to_y

    c_xpos_2 += to_x_2
    c_ypos_2 += to_y_2

    

    if c_xpos > 230 and c_xpos < 350 and c_ypos > 0 and c_ypos < 300:
        to_x = 0
        to_y = 0
    if c_xpos_2 > 230 and c_xpos_2 < 350 and c_ypos_2 > 0 and c_ypos_2 < 300:
        to_x_2 = 0
        to_y_2 = 0

    if c_xpos > 625 and c_xpos < 750 and c_ypos > 220 and c_ypos < 600:
        to_x = 0
        to_y = 0
    if c_xpos_2 > 625 and c_xpos_2 < 750 and c_ypos_2 > 220 and c_ypos_2 < 600:
        to_x_2 = 0
        to_y_2 = 0



    if c_xpos < 0:
        c_xpos = 0

    elif c_xpos > screen_width - c_width:
        c_xpos = screen_width - c_width

    if c_ypos < 0:
        c_ypos = 0
    elif c_ypos > screen_height - c_height:
        c_ypos = screen_height - c_height
    
    character_rect = c.get_rect()
    character_rect.left = c_xpos
    character_rect.top = c_ypos

    exit_rect = ex.get_rect()
    exit_rect.left = ex_xpos
    exit_rect.top = ex_ypos

    character_2_rect = c_2.get_rect()
    character_2_rect.left = c_xpos_2
    character_2_rect.top = c_ypos_2

    enemy_rect = e.get_rect()
    enemy_rect.left = e_xpos
    enemy_rect.top = e_ypos

    wall_rect = w.get_rect()
    wall_rect.left = w_xpos
    wall_rect.top = w_ypos

    wall_2_rect = w_2.get_rect()
    wall_2_rect.left = w_xpos_2
    wall_2_rect.top = w_ypos_2

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        if 충돌함 == 0:
            player_speed = 10.0
            보석먹음 = 1
            충돌함 = 1
            e_xpos = 10000

    if character_rect.colliderect(exit_rect):
        if 보석먹음 == 1:
            screen.blit(player_win,(0,0))
            print("플레이어 이김")
            winning = 1
            running = False

        

        

    if character_rect.colliderect(character_2_rect):
        screen.blit(Sulwin,(0,0))
        print("술래 이김")
        winning = 2
        running = False

    if character_2_rect.colliderect(enemy_rect):
        c_xpos_2 = 920
        c_ypos_2 = 520

    if character_2_rect.colliderect(exit_rect):
        c_xpos_2 = 920
        c_ypos_2 = 520

    # if character_2_rect.colliderect(wall_rect):
    #     c_xpos_2 = 920
    #     c_ypos_2 = 520

    # if character_2_rect.colliderect(wall_2_rect):
    #     c_xpos_2 = 920
    #     c_ypos_2 = 520
        
    # if character_rect.colliderect(wall_rect):
    #     c_xpos = 0
    #     c_ypos = 0

    # if character_rect.colliderect(wall_2_rect):
    #     c_xpos = 0
    #     c_ypos = 0
    
    

    if c_xpos_2 < 0:
        c_xpos_2 = 0

    elif c_xpos_2 > screen_width - c_width_2:
        c_xpos_2 = screen_width - c_width_2

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    if c_ypos_2 < 0:
        c_ypos_2 = 0
    elif c_ypos_2 > screen_height - c_height_2:
        c_ypos_2 = screen_height - c_height_2

    ################################################

    if int(total_time - elapsed_time) == 0:
        screen.blit(Mu,(0,0))
        print("무승부")
        winning = 3
        running = False


    screen.fill((100, 255, 255))
    #screen.blit(background, (0,0))

    screen.blit(e, (e_xpos, e_ypos))

    screen.blit(c, (c_xpos,c_ypos))
    
    screen.blit(c_2, (c_xpos_2,c_ypos_2))

    screen.blit(ex, (ex_xpos,ex_ypos))

    screen.blit(w, (w_xpos,w_ypos))

    screen.blit(w_2, (w_xpos_2,w_ypos_2))

    

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer, (500,0))


    pygame.display.update()

#########################Ending################################

while winning != 0:
    if winning == 1: screen.blit(player_win, (0,0))
    if winning == 3: screen.blit(Mu, (0,0))
    if winning == 2: screen.blit(Sulwin, (0,0))
    
    
    winning = 0
    
    pygame.display.update()


t.sleep(3)

pygame.quit()