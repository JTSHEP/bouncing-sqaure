import random, math, pygame
from pygame.locals import *

WINSIZE = [640, 480]
WINCENTER = [320, 240]
speed = [1,1]


def main():
     screen = pygame.display.set_mode(WINSIZE)
     pygame.display.set_caption('Test')
     black = 20, 20, 40
     screen.fill(black)
     square = pygame.transform.scale(pygame.image.load("red_square.png"),(50,50))
     rect = square.get_rect()
     rect = rect.move(320,240)
     running = True

     while running:

          pygame.time.wait(int(1000/60))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running = False
               
          rect = rect.move(speed)
          if(rect.top < 0 or rect.bottom > 480):
               speed[1] = -speed[1]
          elif(rect.left < 0 or rect.right > 640):
               speed[0] = -speed[0]
               
          screen.fill(black)
          screen.blit(square, rect)
          pygame.display.flip()

if __name__ == '__main__':
    main()
