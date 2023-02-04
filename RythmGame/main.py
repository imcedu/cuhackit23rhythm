import pygame, os, GameFlow, Draw

WIDTH, HEIGHT = 770, 770
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astro Beats")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
RESTING_JOYSTICK_POSITION = 350


def main():
    clock = pygame.time.Clock()
    game_flow = GameFlow.GameFlow()
    game_flow.draw_title(WIN)
    screen = Draw.Draw()
    run = True

    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_flow.draw_gamescreen(WIN)
                if event.key == pygame.K_ESCAPE:
                    run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()