import pygame
import random
import math

class Ball:

    def __init__(self, position, speed):
        """ Initializes a ball in the middle of 'size' with 'speed'. """
        self.position = position
        self.speed = speed
        self.radius = 20
        self.line_width = 4
        self.color = (255,255,255)

    def step(self, units, size):
        """ Changes the position of ball based on its speed. """
        self.speed.y += 0.1  # gravity effect
        old_position = self.position.copy()
        self.position += self.speed
        if (self.handle_collision_with_other_unit(units)):
            self.position = old_position
        self.stay_on_window(size)
        
    def handle_collision_with_other_unit(self, units):
        """ Check for collisions and respond by swapping speeds. 
        Return 'True' if a collision was detected. 
        """
        for other in units:
            if not other is self:  # don't check collision with itself
                distance = self.position.distance_to(other.position)
                if distance < self.radius + other.radius:  # collision detected
                    other.speed, self.speed = self.speed, other.speed  # swap speeds
                    return True
        return False

    def stay_on_window(self, size):
        """ Keeps the ball on the window. """
        width, height = size
        if self.position.x<self.radius:
            self.position.x = self.radius
            self.speed.x =- self.speed.x
        if self.position.y<self.radius:
            self.position.y=self.radius
            self.speed.y =- self.speed.y
        if self.position.x>width-self.radius:
            self.position.x = width-self.radius
            self.speed.x =- self.speed.x
        if self.position.y>height-self.radius:
            self.position.y=height-self.radius
            self.speed.y =- self.speed.y

    def draw(self, surface):
        """ Draws the ball on the 'surface'. """
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

def random_position(size, margin=20):
    width, height = size
    x = random.randint(margin, width-margin)
    y = random.randint(margin, height-margin)
    return pygame.Vector2(x,y)

def random_speed():
    angle = random.uniform(0, 2*math.pi)
    speed_magnitude = random.uniform(1,3)
    speed_x = speed_magnitude * math.cos(angle)
    speed_y = speed_magnitude * math.sin(angle)
    return pygame.Vector2(speed_x, speed_y)

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('bounce')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    display_size = surface.get_size()
    nr_units = 10
    units = [Ball(random_position(display_size), random_speed()) for _ in range(nr_units)]
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        for unit in units:
            unit.step(units, surface.get_size())
            unit.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
