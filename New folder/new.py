import pygame
import sys

pygame.init()

main = True

i = 0

walkF = ['1','2','3','4']

while main:
  for event in pygame.event.get():
    if event.type == pygame.QUIT :
      pygame.quit()
      sys.exit()
    while event.type == pygame.KEYDOWN :
      if i>3:
        i = 0
      print(walkF[i],(0,0))
      i = i+1
