from circleshape import *
from constants import * 
from logger import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_num = random.uniform(20,50)
        ast_1_vel = self.velocity.rotate(rand_num)
        ast_2_vel = self.velocity.rotate(-rand_num)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position[0],self.position[1],new_rad)
        
        ast1.velocity = ast_1_vel * 1.2
        ast2 = Asteroid(self.position[0],self.position[1],new_rad)

        ast2.velocity = ast_2_vel * 1.2

