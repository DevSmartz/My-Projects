#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame


# In[2]:


import time


# In[3]:


import random


# In[4]:


pygame.font.init()


# In[5]:


WIDTH, HEIGHT = 1000, 800


# In[6]:


WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# In[7]:


pygame.display.set_caption("Space Blaster")

BG = pygame.transform.scale(pygame.image.load("C:\\Users\\Mastermind\\Pictures\\BG.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, "red", player)
    
    pygame.display.update()


# In[ ]:





# In[8]:


def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
                
        draw(player, elapsed_time)
                
    pygame.quit()
    
if __name__=="__main__":
    main()


# In[ ]:




