#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame


# In[2]:


import time


# In[3]:


import random


# In[4]:


WIDTH, HEIGHT = 1000, 800


# In[5]:


WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# In[6]:


pygame.display.set_caption("Space Blaster")

BG = pygame.transform.scale(pygame.image.load("C:\\Users\\Mastermind\\Pictures\\BG.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

def draw(player):
    WIN.blit(BG, (0, 0))
    
    pygame.draw.rect(WIN, "red", player)
    
    pygame.display.update()


# In[ ]:





# In[ ]:


def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                break
        draw(player)
                
    pygame.quit()
    
if __name__=="__main__":
    main()


# In[ ]:




