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

    def draw_flower_images(self, screen, player_inventory):
        # Set up the coordinates for item images
        start_x = self.sprite_rect.x - 317  # Starting position inside the popup
        start_y = self.sprite_rect.y - 268
        gap_x = 12  # Horizontal gap between items

        # Load flower images
        silent_petal_image = pygame.image.load("./Images/Decorations(main)/Decorations.png").subsurface(pygame.Rect(130, 60, 16, 16))  # Placeholder image path
        fire_blush_image = pygame.image.load("./Images/Decorations(main)/Decorations.png").subsurface(pygame.Rect(80, 60, 16, 16))  # Placeholder image path

        # Define font for displaying item counts
        font = pygame.font.Font('./Fonts/Stepalange-x3BLm.otf', 8)

        # Draw Silent Petal if present in inventory
        silent_petal_count = player_inventory.get_item_count('Silent Petal')
        if silent_petal_count > 0:
            screen.blit(silent_petal_image, (start_x, start_y))
            count_surface = font.render(str(silent_petal_count), True, (255, 255, 255))
            screen.blit(count_surface, (start_x + 6, start_y - 2))  # Draw count next to the item image
            start_x += gap_x  # Move x position for the next item

        # Draw Fire Blush if present in inventory
        fire_blush_count = player_inventory.get_item_count('Fire Blush')
        if fire_blush_count > 0:
            screen.blit(fire_blush_image, (start_x, start_y))
            count_surface = font.render(str(fire_blush_count), True, (255, 255, 255))
            screen.blit(count_surface, (start_x + 6, start_y - 2))  # Draw count next to the item image


    def set_visible(self, visible):
        self.visible = visible
