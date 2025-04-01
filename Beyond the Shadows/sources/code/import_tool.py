from csv import reader
from os import walk
import pygame
from csv import reader

def import_csv_layout(path):
    tile_map = []
    with open(path) as tiled_csv:
        layout = reader(tiled_csv,delimiter = ',')
        for row in layout:
            tile_map.append(list(row))
        return tile_map









def import_folder(path):
    
    surface_liste = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_liste.append(image_surf)

    return surface_liste


