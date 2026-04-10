import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

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

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        randAngle = random.uniform(20, 50)
        createdAsteroidOneVector = self.velocity.rotate(randAngle)
        createdAsteroidTwoVector = self.velocity.rotate(-randAngle)
        newRadii= self.radius - ASTEROID_MIN_RADIUS
        newAsteroidOne = Asteroid(self.position.x, self.position.y, newRadii)
        newAsteroidTwo = Asteroid(self.position.x, self.position.y, newRadii)
        newAsteroidOne.velocity = createdAsteroidOneVector * 1.2
        newAsteroidTwo.velocity = createdAsteroidTwoVector * 1.2
        