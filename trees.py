import pygame

class Tree:
    def __init__(self, sprite_sheet_path, sprite_rect, x, y):
        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        # Define the section of the sprite sheet to use (tree)
        self.sprite_rect = sprite_rect
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.sprite_rect.width, self.sprite_rect.height)


    def draw_tree(self, screen, camera):
        # Extract the tree from the sprite sheet and blit it to the screen
        camera_position = camera.apply(self)
        screen.blit(self.sprite_sheet, camera_position, self.sprite_rect)

    def get_rect(self):
        # Return the rect representing the tree's position and size on the screen
        return pygame.Rect(self.x, self.y, self.sprite_rect.width, self.sprite_rect.height)
