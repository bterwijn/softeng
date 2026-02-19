import pygame
import random 

FRAMES_PER_SECOND = 60

def main():
    # initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Polymorphism Game Example")

    # create units
    nr_units = 12
    units = [Unit(screen) for _ in range(nr_units)]

    running = True
    while running:  # run until the user closes the window

        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # user closed the window
                running = False

        # clear the screen
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))

        # step and plot each unit
        for unit in units:
            unit.step(screen)
            unit.plot(screen)
            
        pygame.display.flip()  # update the screen
        pygame.time.Clock().tick(FRAMES_PER_SECOND) # limit frame rate


class Unit:

    def __init__(self, screen):
        """ Initialize a unit """
        self.init_position(screen)
        maxspeed = 5
        self.dx = random.random() * maxspeed * 2 - maxspeed
        self.dy = random.random() * maxspeed * 2 - maxspeed
        self.color = (0, 255, 0) # RGB: Red, Green, Blue
        self.radius = 10

    def init_position(self, screen):
        """ Initialize position of a unit on the screen. """
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())

    def plot(self, screen):
        """ Plot a unit """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

    def step(self, screen):
        """ Take a step: move and possibly other actions. """
        self.move(screen)
        self.handle_border(screen)

    def move(self, screen):
        """ Move a unit """
        self.x += self.dx
        self.y += self.dy
        
    def handle_border(self, screen):
        """ Handle a unit's movement at the edges of the screen. """
        if self.x < 0 or self.x > screen.get_width():
            self.dx = -self.dx
        self.x = max(0, min(self.x, screen.get_width()))
        if self.y < 0 or self.y > screen.get_height():
            self.dy = -self.dy
        self.y = max(0, min(self.y, screen.get_height()))


if __name__ == "__main__":
    main()
