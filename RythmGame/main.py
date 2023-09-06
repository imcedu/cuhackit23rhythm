import pygame as pg, os, GameFlow, Draw, Note, NoteMapper, JoyStick

WIDTH, HEIGHT = 770, 770
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Astro Beats")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
RESTING_JOYSTICK_POSITION = 350
NOTE_OFFSCREEN_SPAWN_OFFSET = 180

#TODO read keybinds from file to set these macros
UP = pg.K_w
DN = pg.K_s
RT = pg.K_d
LT = pg.K_a
SP = pg.K_SPACE

def main():
    clock = pg.time.Clock()
    game_flow = GameFlow.GameFlow()
    game_flow.draw_title(WIN)
    screen = Draw.Draw()
    run = True
    started = False
    mapper = NoteMapper.NoteMapper()
    stick = JoyStick.JoyStick(RESTING_JOYSTICK_POSITION, RESTING_JOYSTICK_POSITION, RED)
    map = mapper.map
    currNotes = []

    while(run):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                # Strum JoyStick if space was pressed during the tick
                if event.key == SP:
                    stick.strum()
                    for note in currNotes:
                        if game_flow.does_collide(stick, note, WIN):
                            screen.explosion(note, WIN)
                            screen.erase(note)
                            currNotes.remove(note)
                if event.key == DN:
                    if not started:
                        screen.draw(WIN)
                        started = True
                        frameCounter = -1 #incremented at end of every tick, so will start at 0
                        #TODO: play the song here
                        game_flow.play_backtrack()
                if event.key == pg.K_ESCAPE:
                    run = False
        if started:
            # Move JoyStick in direction
            keys_pressed = pg.key.get_pressed()
            stick.move_stick(WIN, keys_pressed, screen)

            frameCounter += 1
            if int(map[0][1]) - frameCounter <= NOTE_OFFSCREEN_SPAWN_OFFSET:
                 startXpos, startYpos  = getStartPos(map[0][0])
                 note = Note.Note(screen, map[0][0], startXpos, startYpos, NOTE_OFFSCREEN_SPAWN_OFFSET / FPS)
                 currNotes.append(note)
                 map.pop(0)
            for n in currNotes:
                n.moveIn(screen, n.xDir, n.yDir, n.speed)
                if (n.destroyable):
                    currNotes.remove(n)
                    
            screen.draw(WIN)
        
        # Reset JoyStick
        stick.reset_stick(RESTING_JOYSTICK_POSITION, screen)

    pg.quit()

def getStartPos(direction):
    match direction:
        # C_UP = 0,
        case 0:
            return ((WIDTH * 0.5), (HEIGHT + HEIGHT * 0.5))
        
        # C_DOWN = 1,
        case 1:
            return ((WIDTH * 0.5), (0 - HEIGHT * 0.5))

        # C_LEFT = 2,
        case 2:
            return ((WIDTH + WIDTH * 0.5), (HEIGHT * 0.5))
            
        # C_RIGHT = 3,
        case 3:
            return ((0 - WIDTH * 0.5), (HEIGHT * 0.5))

        # D_UPLEFT = 4,
        case 4:
            return ((WIDTH + WIDTH * 0.5), (HEIGHT + HEIGHT * 0.5))

        # D_UPRIGHT = 5,
        case 5:
            return ((0 - WIDTH * 0.5), (HEIGHT + HEIGHT * 0.5))

        # D_DNRIGHT = 6,
        case 6:
            return ((0 - WIDTH * 0.5), (0 - HEIGHT * 0.5))

        # D_DNLEFT = 7,
        case 7:
            return ((WIDTH + WIDTH * 0.5), (0 - HEIGHT * 0.5))

if __name__ == "__main__":
    main()