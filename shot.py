from circleshape import CircleShape
from constants import SHOT_RADIUS,LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x_cord, y_cord) -> None:
        super().__init__(x_cord,y_cord,SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position += (self.velocity * dt)