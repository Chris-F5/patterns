import pygame
import argparse
import importlib
import numpy as np
import time
import os
import sys

np.random.seed(42)
import pattern

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
args = parser.parse_args()

pygame.init()
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pygame.display.set_caption("Pattern")
clock = pygame.time.Clock()


otime = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    ctime = os.path.getmtime('pattern.py')
    if ctime != otime:
        print("reload")
        print(sys.getrefcount(pattern))
        time.sleep(0.1)
        np.random.seed(42)
        importlib.invalidate_caches()
        pattern = importlib.reload(pattern)
        otime = ctime
        print(pattern.testfun())
    pattern.draw(screen)
    pygame.display.flip()
    clock.tick(60)
