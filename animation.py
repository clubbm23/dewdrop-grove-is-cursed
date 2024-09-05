# animation.py
import pygame

class Animation:
    def __init__(self, frame_paths, frame_delay):
        self.frames = [pygame.image.load(path) for path in frame_paths]
        self.frame_count = len(self.frames)
        self.current_frame = 0
        self.frame_delay = frame_delay
        self.last_update = pygame.time.get_ticks()
        
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_delay:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update = now
            
    def get_current_frame(self):
        return self.frames[self.current_frame]
