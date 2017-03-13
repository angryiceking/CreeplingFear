from __future__ import absolute_import, division, print_function
from pygame.locals import *
from itertools import cycle
from sprites import Spritesheet
from maps import main_map
import pygame, os, sys, time

WHITE = (236, 240, 241)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BG = (0, 0, 0)
BLINK_EVENT = pygame.USEREVENT + 0

pygame.init()
disp = pygame.display.set_mode((640, 360))
disp_rect = disp.get_rect()
title = pygame.font.Font('utils/fonts/8-BIT WONDER.TTF', 20)
font = pygame.font.Font('utils/fonts/8-BIT WONDER.TTF', 10)
fq = pygame.font.Font('utils/fonts/8-BIT WONDER.TTF', 8)
mapfont = pygame.font.Font('utils/fonts/unifont-9.0.06.ttf', 8)

render_title = title.render('CREEPLING FEAR', True, WHITE)
render_f = fq.render('Press Q or ESC to Exit', True, WHITE)
fstage = mapfont.render(main_map(), True, WHITE)
title_rect = render_title.get_rect()
title_rect.center = (300, 500)

ss = Spritesheet('rpgcritters2.png')
image = ss.image_at((0, 0, 16, 16))
images = []

# images = ss.images_at((0, 0, 16, 16), (17, 0, 16, 16), colorkey=(255, 255, 255))

def start_game():
    disp.fill(BG)

def animate_text(s):
    for c in s:
        sys.stdout.write( '%s' %c)
        sys.stdout.flush()
        time.sleep(0.05)

def main():
    try:
        title_screen = True
    	clock = pygame.time.Clock()

    	pygame.display.set_caption('Creepling Fear')
    	on_text_surface = font.render(
                'Press any key to start', True, WHITE
        )
	blink_rect = on_text_surface.get_rect()
        blink_rect.center = disp_rect.center
        off_text_surface = pygame.Surface(blink_rect.size)
        blink_surfaces = cycle([on_text_surface, off_text_surface])
        blink_surface = next(blink_surfaces)
        if title_screen == True:
            pygame.time.set_timer(BLINK_EVENT, 500)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == BLINK_EVENT and title_screen == True:
                    blink_surface = next(blink_surfaces)
                elif event.type == pygame.KEYDOWN:
                    if  event.type == pygame.KEYDOWN:
                        disp.fill((0, 0, 0))
                        pygame.display.update()
                    if  event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        return
                    if  event.key == pygame.K_w:
                        print("you walked forward, didn't you?")
                    elif  event.key == pygame.K_a:
                        print("you walked sideward to the left, didn't you?")
                    elif  event.key == pygame.K_s:
                        print("you walked backward, didn't you?")
                    elif  event.key == pygame.K_d:
                        print("you walked sideward right, didn't you?")

            disp.blit(render_f, (240, 340))
            disp.blit(render_title, (190, 100))
            disp.blit(blink_surface, blink_rect)
            pygame.display.update()
            clock.tick(260)
    finally:
        pygame.quit()

if __name__ == '__main__':
       main()
