import pygame

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)

class Player():
    __init__(self):
        health = 10
        score = 0
    
    lose_hp(self):
        health -= 1

    increment_score(self):
        score += 1
