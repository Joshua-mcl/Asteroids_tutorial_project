from circleshape import *
from constants import * 
from pygame.math import Vector2
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(PLAYER_RADIUS,x,y)
        self.position = Vector2(x,y)
        self.radius = PLAYER_RADIUS
    
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen,"white",points, 2)
   
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt





#to draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon. It takes:
#The screen object
#A color (use "white")
#A list of points (use self.triangle() that we provided for you)
#A line width (use 2)
