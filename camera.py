import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """Apply the camera offset to an entity."""
        return entity.rect.move(self.camera_rect.topleft)

    def update(self, target):
        """Update the camera's position to follow the target (player)."""
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Keep the camera within bounds (prevent showing outside the scene if there are edges)
        x = min(0, x)  # Left edge
        y = min(0, y)  # Top edge
        x = max(-(self.width - target.rect.width), x)  # Right edge
        y = max(-(self.height - target.rect.height), y)  # Bottom edge

        self.camera_rect = pygame.Rect(x, y, self.width, self.height)

import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """Apply the camera offset to an entity."""
        return entity.rect.move(self.camera_rect.topleft)

    def update(self, target):
        """Update the camera's position to follow the target (player)."""
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Keep the camera within bounds (prevent showing outside the scene if there are edges)
        x = min(0, x)  # Left edge
        y = min(0, y)  # Top edge
        x = max(-(self.width - target.rect.width), x)  # Right edge
        y = max(-(self.height - target.rect.height), y)  # Bottom edge

        self.camera_rect = pygame.Rect(x, y, self.width, self.height)
