import pygame
from trees import Tree
from flowers import Flower
import random

MIN_TREE_DISTANCE = 2
MIN_FLOWER_DISTANCE = 1

blue_flower_rect = pygame.Rect(130, 60, 16, 16)
pink_flower_rect = pygame.Rect(80, 60, 16, 16)

class Orchard:
    def __init__(self, screen, background_image):
        self.trees = []
        self.flowers = []
        self.screen = screen
        self.background_image = background_image

    def add_tree(self, tree):
        self.trees.append(tree)

    def add_flower(self, flower):
        self.flowers.append(flower)

    def draw_orchard(self, camera):
        # Draw the orchard's background and all the objects with camera offsets
        for tree in self.trees:
            tree.draw_tree(self.screen, camera)

        # Draw all flowers relative to the camera
        for flower in self.flowers:
            flower.draw_flower(self.screen, camera)

    def can_place_tree(self, new_tree_rect):
        # Check if the new tree can be placed without overlapping existing trees
        for tree in self.trees:
            existing_tree_rect = tree.get_rect()
            if existing_tree_rect.colliderect(new_tree_rect.inflate(MIN_TREE_DISTANCE, MIN_TREE_DISTANCE)):
                return False
        return True

    def place_tree(self, tree):
        if self.can_place_tree(tree.get_rect()):
            self.add_tree(tree)
            return True
        return False
    
    def can_place_flower(self, new_flower_rect):
        # Check if the new flower can be placed without overlapping existing trees or flowers
        for flower in self.flowers:
            existing_flower_rect = flower.get_rect()
            if existing_flower_rect.colliderect(new_flower_rect.inflate(MIN_FLOWER_DISTANCE, MIN_FLOWER_DISTANCE)):
                return False
        for tree in self.trees:
            existing_tree_rect = tree.get_rect()
            if existing_tree_rect.colliderect(new_flower_rect.inflate(MIN_FLOWER_DISTANCE, MIN_FLOWER_DISTANCE)):
                return False
        return True

    def place_flower(self, flower):
        if self.can_place_flower(flower.get_rect()):
            self.add_flower(flower)
            return True
        return False

    def remove_flower(self, flower_to_remove):
        # Remove the flower from the list
        self.flowers = [flower for flower in self.flowers if flower != flower_to_remove]
        
        # Define flower spawn ranges
        flower_spawn_ranges = {
            'blue': (0, 1000, 0, 1000),
            'pink': (0, 1000, 0, 1000)
        }

        # Get the color of the removed flower
        if flower_to_remove.sprite_rect == blue_flower_rect:
            color = 'blue'
        elif flower_to_remove.sprite_rect == pink_flower_rect:
            color = 'pink'
        else:
            return  

        # Get spawn ranges based on flower color
        x_min, x_max, y_min, y_max = flower_spawn_ranges[color]
        new_x = random.randint(x_min, x_max - flower_to_remove.sprite_rect.width)
        new_y = random.randint(y_min, y_max - flower_to_remove.sprite_rect.height)

        # Create and place a new flower
        new_flower = Flower(flower_to_remove.sprite_sheet, flower_to_remove.sprite_rect, new_x, new_y)
        self.place_flower(new_flower)