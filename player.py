import pygame
from inventory import Inventory

class Player:
    def __init__(self, walking_images, idle_images, x, y, background_width, background_height):
        self.walking_images = walking_images  # These are now images, not paths
        self.idle_images = idle_images  # These are now images, not paths
        self.x = x
        self.y = y
        self.width = self.walking_images[0].get_width()  # Get width from the actual image
        self.height = self.walking_images[0].get_height()

        # Adjust the rect size based on the scaled image
        self.rect_width = self.width
        self.rect_height = self.height

        # Centering the rectangle on the image
        self.image = self.idle_images[0]
        self.rect = pygame.Rect(
            self.x - self.rect_width // 2,
            self.y - self.rect_height // 2,
            self.rect_width,
            self.rect_height
        )
        self.speed = 2
        self.direction = 'RIGHT'
        self.current_frame = 0
        self.animation_speed = 0.1
        self.idle_animation_timer = 0
        self.is_moving = False
        self.collision_margin = 0.9

        self.inventory = Inventory()

    def draw_player(self, screen, camera):
        # Apply the camera offset when drawing the player
        camera_position = camera.apply(self)
        screen.blit(self.image, camera_position)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-self.speed, 0, 'LEFT')
            self.is_moving = True
        elif keys[pygame.K_RIGHT]:
            self.move(self.speed, 0, 'RIGHT')
            self.is_moving = True
        elif keys[pygame.K_UP]:
            self.move(0, -self.speed, self.direction)
            self.is_moving = True
        elif keys[pygame.K_DOWN]:
            self.move(0, self.speed, self.direction)
            self.is_moving = True
        else:
            self.is_moving = False

        self.update()

    def move(self, dx, dy, direction):
        self.rect.x += dx
        self.rect.y += dy
        self.direction = direction

        # Check collision with trees
        if self.check_collision():
            self.rect.x -= dx
            self.rect.y -= dy

        self.x = self.rect.centerx
        self.y = self.rect.centery

    def check_collision(self):
        # Check collision with trees, ensuring a margin for the player to get close but not overlap
        for tree in self.trees:
            tree_rect = tree.get_rect().inflate(self.collision_margin, self.collision_margin)
            if self.rect.colliderect(tree_rect):
                return True
        return False

    def update(self):
        if self.is_moving:
            if self.direction == 'LEFT':
                self.image = pygame.transform.flip(self.walking_images[int(self.current_frame)], True, False)
            else:
                self.image = self.walking_images[int(self.current_frame)]
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.walking_images):
                self.current_frame = 0
        else:
            self.image = self.idle_images[int(self.idle_animation_timer)]
            self.idle_animation_timer += self.animation_speed
            if self.idle_animation_timer >= len(self.idle_images):
                self.idle_animation_timer = 0

    def set_trees(self, trees):
        self.trees = trees

    def add_item_to_inventory(self, item_name, quantity=1):
        self.inventory.add_item(item_name, quantity)

    def remove_item_from_inventory(self, item_name, quantity=1):
        self.inventory.remove_item(item_name, quantity)

    def get_inventory(self):
        return self.inventory

    def list_inventory(self):
        return self.inventory.get_items() if self.inventory else {}
    
    def get_rect(self):
        return self.rect
