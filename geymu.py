from __future__ import absolute_import, division, print_function
from pygame.locals import *
from itertools import cycle
import pygame, os, sys, time

WHITE = (236, 240, 241)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLINK_EVENT = pygame.USEREVENT + 0

pygame.init()
disp = pygame.display.set_mode((640, 360))
disp_rect = disp.get_rect()
title = pygame.font.Font('8-BIT WONDER.TTF', 15)
font = pygame.font.Font('8-BIT WONDER.TTF', 10)

render_title = title.render('This is the Title', True, WHITE)
title_rect = render_title.get_rect()
title_rect.center = (300, 500)

def animate_text(s):
    for c in s:
        sys.stdout.write( '%s' %c)
        sys.stdout.flush()
        time.sleep(0.05)

def main():
    try:
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
        pygame.time.set_timer(BLINK_EVENT, 700)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)
                elif event.type == pygame.KEYDOWN:
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

            disp.blit(render_title,(210, 50))
            disp.blit(blink_surface, blink_rect)
            pygame.display.update()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == '__main__':
       main()
