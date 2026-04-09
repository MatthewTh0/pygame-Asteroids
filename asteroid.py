import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    #def move(self, dt):
        #unit_vector = pygame.Vector2(0, 1)
        #rotated_vector = unit_vector.rotate(self.rotation)
        #rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        #self.position += rotated_with_speed_vector

        