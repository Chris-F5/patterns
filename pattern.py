import numpy as np
import pygame

colors = np.array([
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
color_bg = pygame.Color(0, 0, 0, 0)

def testfun():
    return 2
scale = 2
size = 200

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
points_color = np.random.randint(0, len(colors), size=point_count)
delta = np.random.uniform(size=(point_count, 2)) * 0.02

def draw(screen):
    grid = voroni_diagram(points, points_weight)
    x = points_color[grid]

    screen.fill(color_bg)
    surface = pygame.surfarray.make_surface(colors[x])
    surface = pygame.transform.scale(surface, (size*scale, size*scale))
    screen.blit(surface, (0,0))
