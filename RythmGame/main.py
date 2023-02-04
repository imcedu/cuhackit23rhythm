import pygame, Draw

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    screen = Draw.Draw()
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.draw(WIN)

    pygame.quit()

if __name__ == "__main__":
    main()