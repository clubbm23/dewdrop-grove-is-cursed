import pygame

class Flower:
    def __init__(self, sprite_sheet_path, sprite_rect, x, y):
        sprite_sheet_path = "./Images/Decorations(main)/Decorations.png"
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.sprite_rect = sprite_rect
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.sprite_rect.width, self.sprite_rect.height)
        self.visible = True  # New attribute to control visibility

    def draw_flower(self, screen, camera):
        if self.visible:  # Only draw if visible
            camera_position = camera.apply(self)
            screen.blit(self.sprite_sheet, camera_position, self.sprite_rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.sprite_rect.width, self.sprite_rect.height)

    def hide(self):
        self.visible = False

    def is_visible(self):
        return self.visible
