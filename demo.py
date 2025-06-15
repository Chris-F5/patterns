import pygame
import PIL.Image
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
args = parser.parse_args()

pygame.init()

scale = 4
size = 200

# xcolor "-c [%{r}, %{g}, %{b}],"

color_bg = pygame.Color(255, 255, 255, 0)
colors = np.array([
    [220, 220, 180],
    [0, 146, 69],
    [0, 181, 82],
    [1, 174, 78],
    [2, 7, 37],
    [2, 46, 118],
    [3, 4, 37],
    [4, 34, 93],
    [4, 107, 52],
    [6, 88, 188],
    [117, 189, 230],
    [135, 198, 243],
    [141, 210, 249],
    [168, 155, 184],
    [188, 176, 205],
    [189, 175, 206],
    [192, 110, 30],
    [203, 94, 96],
    [228, 0, 11],
    [235, 121, 129],
    [239, 82, 64],
    [242, 75, 61],
    [252, 150, 38],
    [253, 82, 53],
    [254, 159, 33],
    [255, 50, 8],
])

screen = pygame.display.set_mode((scale*size, scale*size))
pygame.display.set_caption("Pattern")
clock = pygame.time.Clock()

def voroni_diagram(points, weights):
    x, y = np.meshgrid(np.arange(size), np.arange(size))
    px, py = points.T
    dx = x[:,:,np.newaxis] - px
    dy = y[:,:,np.newaxis] - py
    d = (np.square(dx) + np.square(dy)) / weights
    grid = np.argmin(d, axis=2)
    return grid

point_count = 50
points = np.random.uniform(size=(point_count, 2)) * size
points_weight = np.random.uniform(1, 4, size=point_count)
points_color = np.random.randint(1, len(colors), size=point_count)
delta = np.random.uniform(size=(point_count, 2)) * 0.02

t = 0
saved = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # UPDATE
    points += delta
    mx,my = pygame.mouse.get_pos()
    points[0][0] = my/scale
    points[0][1] = mx/scale
    #points_weight[0] = 0.1
    points_color[0] = 0
    grid = voroni_diagram(points, points_weight)
    x = points_color[grid]

    # Render
    screen.fill(color_bg)

    surface = pygame.surfarray.make_surface(colors[x])
    surface = pygame.transform.scale(surface, (size*scale, size*scale))
    screen.blit(surface, (0,0))

    pygame.display.flip()
    clock.tick(60)
