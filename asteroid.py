from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            x, y = self.position
            angle = random.uniform(20, 50)
            velocity_one = self.velocity.rotate(angle)
            velocity_two = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            new_one = Asteroid(x, y, radius)
            new_two = Asteroid(x, y, radius)
            new_one.velocity = velocity_one * 1.2
            new_two.velocity = velocity_two * 1.2
