import pygame

class Popup:
    def __init__(self, sprite_sheet_path, sprite_rect, screen_width, screen_height):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.sprite_rect = pygame.Rect(450, 110, 100, 80)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.visible = False
        self.flower_images = {
            'Silent Petal': pygame.image.load("./Images/Decorations(main)/Decorations.png").subsurface(pygame.Rect(130, 60, 16, 16)),
            'Fire Blush': pygame.image.load("./Images/Decorations(main)/Decorations.png").subsurface(pygame.Rect(80, 60, 16, 16))
        }
        self.flower_counts = {'Silent Petal': 0, 'Fire Blush': 0}

        # Center the popup
        self.sprite_rect = pygame.Rect(
            (self.screen_width - sprite_rect.width),
            (self.screen_height - sprite_rect.height),
            sprite_rect.width,
            sprite_rect.height
        )

        self.font = pygame.font.Font('./Fonts/Stepalange-x3BLm.otf', 24)

    def draw(self, screen):
        if self.visible:
            popup_position = (self.screen_width - self.sprite_rect.width - 350,  # Right edge padding
                              250)  # Top padding
            screen.blit(self.sprite_sheet, popup_position, pygame.Rect(450, 110, 100, 80))
            text_surface = self.font.render('Inventory', True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(popup_position[0] + self.sprite_rect.width // 2, popup_position[1] - 20))  # Position above popup
            screen.blit(text_surface, text_rect)

    def draw_flower_images(self, screen):
        start_x = self.sprite_rect.x + 10
        start_y = self.sprite_rect.y + 10

        for flower, image in self.flower_images.items():
            count = self.flower_counts.get(flower, 0)
            if count > 0:
                # Draw the flower image
                screen.blit(image, (start_x, start_y))

                # Draw the count text
                font = pygame.font.Font('./Fonts/Stepalange-x3BLm.otf', 24)
                count_text = font.render(str(count), True, (0, 0, 0))
                screen.blit(count_text, (start_x + image.get_width() - count_text.get_width(), start_y + image.get_height() - count_text.get_height()))

                # Update starting position for the next flower
                start_x += image.get_width() + 10

    def update_flower_counts(self, inventory):
        """Update flower counts based on the inventory."""
        self.flower_counts = {flower: inventory.get_items().get(flower, 0) for flower in self.flower_images.keys()}

    def set_visible(self, visible):
        self.visible = visible
