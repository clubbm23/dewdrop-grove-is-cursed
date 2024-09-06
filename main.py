import pygame
import random
import camera
import orchard
import player
from trees import Tree
from flowers import Flower
from orchard import Orchard
from player import Player
from camera import Camera
from popup import Popup

# Initialize pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
MIN_TREE_DISTANCE = 2
MIN_FLOWER_DISTANCE = 1
PLAYER_START_X = SCREEN_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT // 2

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dewdrop Grove Cursed")

# Load the background image
background_image = pygame.image.load("./Images/green.jpg")

# Create the inventory pop-up
sprite_sheet_path = "./Images/InventorySlots.png"
inventory_popup_rect = pygame.Rect(450, 110, 100, 80)
inventory_popup = Popup(sprite_sheet_path, inventory_popup_rect, SCREEN_WIDTH, SCREEN_HEIGHT)

def main():
    orchard = Orchard(screen, background_image)
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    # TREES
    little_tree_rect = pygame.Rect(158, 106, 33, 33)
    big_tree_rect = pygame.Rect(208, 85, 50, 60)
    little_tree_count = 0
    big_tree_count = 0

    while little_tree_count < 70:
        littleTree = Tree("./Images/Decorations(main)/Decorations.png", little_tree_rect, random.randint(0, 1380 - little_tree_rect.width), random.randint(0, 920 - little_tree_rect.height))
        if orchard.place_tree(littleTree):
            little_tree_count += 1

    while big_tree_count < 40:
        bigTree = Tree("./Images/Decorations(main)/Decorations.png", big_tree_rect, random.randint(0, 1880 - big_tree_rect.width), random.randint(0, 1220 - big_tree_rect.height))
        if orchard.place_tree(bigTree):
            big_tree_count += 1

    # FLOWERS
    blue_flower_rect = pygame.Rect(130, 60, 16, 16)
    pink_flower_rect = pygame.Rect(80, 60, 16, 16)
    blue_flower_count = 0
    pink_flower_count = 0

    while blue_flower_count < 100:
        blueFlower = Flower("./Images/Decorations(main)/Decorations.png", blue_flower_rect, random.randint(0, 2080 - blue_flower_rect.width), random.randint(0, 1500 - blue_flower_rect.height))
        if orchard.place_flower(blueFlower):
            blue_flower_count += 1

    while pink_flower_count < 160:
        pinkFlower = Flower("./Images/Decorations(main)/Decorations.png", pink_flower_rect, random.randint(0, 2000 - pink_flower_rect.width), random.randint(0, 1500 - pink_flower_rect.height))
        if orchard.place_flower(pinkFlower):
            pink_flower_count += 1

    # PLAYER
    walking_image_paths = [
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_0.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_1.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_2.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_3.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_4.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_5.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_6.png",
        "./Images/Female/Character 1/Clothes 1/walk/Character1F_1_walk_7.png"
    ]
    idle_image_paths = [
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_0.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_1.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_2.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_3.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_4.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_5.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_6.png",
        "./Images/Female/Character 1/Clothes 1/idle/Character1F_1_idle_7.png"
    ]
    player = Player(walking_image_paths, idle_image_paths, PLAYER_START_X, PLAYER_START_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
    player.set_trees(orchard.trees)

    clock = pygame.time.Clock()

    inventory_visible = False
    inventory_toggle = False

    # Main game loop
    running = True
    while running:

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player movement and animation
        player.handle_keys()
        player.update()

        # Update camera to follow player
        camera.update(player)

        # Draw orchard
        orchard.draw_orchard(camera)

        # Draw player
        player.draw_player(screen, camera)

        # Handle inventory toggle with key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i] and not inventory_toggle:
            inventory_visible = True
            inventory_popup.set_visible(True)  # Show the popup
            inventory_toggle = True  # Set the toggle to prevent retrigger

        # Check for 'ESC' key to close the inventory
        if keys[pygame.K_ESCAPE]:
            inventory_visible = False
            inventory_popup.set_visible(False)  # Hide the popup
            inventory_toggle = False  # Reset the toggle

        # Make sure inventory_toggle is reset when the key is no longer pressed
        if not keys[pygame.K_i] and inventory_toggle:
            inventory_toggle = False

        # Draw inventory popup if visible
        if inventory_popup.visible:
            inventory_popup.draw(screen)
            inventory_popup.draw_flower_images(screen, player.get_inventory())
            


        for flower in orchard.flowers:
            if flower.visible and player.get_rect().colliderect(flower.get_rect()):
                if keys[pygame.K_e]:
                    if flower.sprite_rect == blue_flower_rect:
                        player.add_item_to_inventory("Silent Petal")
                        orchard.remove_flower(flower)  # Remove the flower from the orchard

        for flower in orchard.flowers:
            if flower.visible and player.get_rect().colliderect(flower.get_rect()):
                if keys[pygame.K_e]:
                    if flower.sprite_rect == pink_flower_rect:
                        player.add_item_to_inventory("Fire Blush")
                        orchard.remove_flower(flower)  # Remove the flower from the orchard

        # Draw inventory counts
        font = pygame.font.Font('./Fonts/Stepalange-x3BLm.otf', 24)
        silent_petal_count = player.inventory.get_item_count('Silent Petal')  # Assuming you have a get_item_count method
        fire_blush_count = player.inventory.get_item_count('Fire Blush')
        text = f"Silent Petal: {silent_petal_count}, Fire Blush: {fire_blush_count}"
        text_surface = font.render(text, True, (225, 225, 225))
        screen.blit(text_surface, (10, 10))

        # Update display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)  # type: ignore # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
