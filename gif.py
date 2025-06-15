import pygame
import PIL.Image
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
args = parser.parse_args()

pygame.init()

scale = 10
size = 50

color_bg = pygame.Color(0, 255, 0, 100)

screen = pygame.display.set_mode((scale*size, header+scale*size))
pygame.display.set_caption("Search Algorithms")
clock = pygame.time.Clock()

#font_name = pygame.font.match_font("DejaVu Sans Mono")
#font = pygame.font.Font(font_name)
#header_text = font.render(name, True, header_color)
#header_text_rect = header_text.get_rect()
#header_text_rect.center = (scale*size//2, header//2)

#s = pygame.Surface((scale,scale))
#s.fill(col)
#s.set_alpha(col.a)
#for (x,y) in cells:
#    screen.blit(s, (x*scale, y*scale+header))

frames = []
t = 0
saved = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Render
    screen.fill("white")
    screen.blit(header_text, header_text_rect)
    draw_cells(screen, map.walls(), wall_color)
    draw_cells(screen, path, path_color)
    draw_cells(screen, map.search_list[:t], search_color)

    pygame.display.flip()
    clock.tick(60)
    if t < len(map.search_list):
        image = pygame.surfarray.array3d(screen)
        image = np.transpose(image, (1, 0, 2))
        pil = PIL.Image.fromarray(image)
        frames.append(pil)
        t += 1
    elif not saved and args.output:
        frames[0].save(
            args.output,
            save_all=True,
            optimize=False,
            append_images=frames[1:],
            loop=0,
            duration=10,
        )
        saved = True
        raise SystemExit

