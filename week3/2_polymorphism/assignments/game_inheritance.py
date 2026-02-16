import pygame
import random

from pyparsing import ABC, abstractmethod

FRAMES_PER_SECOND = 60

def main():
    # initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Polymorphism Game Example")

    # create units
    nr_units = 12
    unit_types = [
                    lambda screen: Unit_Random_Start_Bounce(screen), 
                    lambda screen: Unit_Random_Start_Wraparound(screen), 
                    lambda screen: Unit_Center_Start_Bounce(screen),
                    lambda screen: Unit_Center_Start_Wraparound(screen)
                  ]
    units = [unit_types[i % len(unit_types)](screen) for i in range(nr_units)]

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


class Unit_Base(ABC):

    def __init__(self, screen, color =(0, 255, 0)):
        """ Initialize a unit """
        self.init_position(screen)
        maxspeed = 5
        self.dx = random.random() * maxspeed * 2 - maxspeed
        self.dy = random.random() * maxspeed * 2 - maxspeed
        self.color = color
        self.radius = 10

    @abstractmethod
    def init_position(self, screen):
        """ Initialize position of a unit """
        ...

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

    @abstractmethod
    def handle_border(self, screen):
        """ Handle a unit's movement at the edges of the screen. """
        ...

class Unit_Random_Start(Unit_Base):

    def init_position(self, screen):
        self.x = random.random() * screen.get_width()
        self.y = random.random() * screen.get_height()

class Unit_Random_Start_Bounce(Unit_Random_Start):

    def __init__(self, screen):
        super().__init__(screen, color=(255, 0, 0))

    def handle_border(self, screen):
        if self.x < 0 or self.x > screen.get_width():
            self.dx = -self.dx
        self.x = max(0, min(self.x, screen.get_width()))
        if self.y < 0 or self.y > screen.get_height():
            self.dy = -self.dy
        self.y = max(0, min(self.y, screen.get_height()))

class Unit_Random_Start_Wraparound(Unit_Random_Start):

    def __init__(self, screen):
        super().__init__(screen, color=(100, 0, 0))

    def handle_border(self, screen):
        if self.x < 0:
            self.x = screen.get_width()
        if self.x > screen.get_width():
            self.x = 0
        if self.y < 0:
            self.y = screen.get_height()
        if self.y > screen.get_height():
            self.y = 0

class Unit_Center_Start(Unit_Base):

    def init_position(self, screen):
        self.x = screen.get_width() // 2
        self.y = screen.get_height() // 2

class Unit_Center_Start_Bounce(Unit_Center_Start):

    def __init__(self, screen):
        super().__init__(screen, color=(0, 0, 255))

    def handle_border(self, screen):
        if self.x < 0 or self.x > screen.get_width():
            self.dx = -self.dx
        self.x = max(0, min(self.x, screen.get_width()))
        if self.y < 0 or self.y > screen.get_height():
            self.dy = -self.dy
        self.y = max(0, min(self.y, screen.get_height()))

class Unit_Center_Start_Wraparound(Unit_Center_Start):

    def __init__(self, screen):
        super().__init__(screen, color=(0, 0, 100))

    def handle_border(self, screen):
        if self.x < 0:
            self.x = screen.get_width()
        if self.x > screen.get_width():
            self.x = 0
        if self.y < 0:
            self.y = screen.get_height()
        if self.y > screen.get_height():
            self.y = 0

if __name__ == "__main__":
    main()
