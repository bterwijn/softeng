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
                    lambda screen: Unit(screen, Position_Random_Start(), Border_Bounce(), color =(255, 0, 0)), 
                    lambda screen: Unit(screen, Position_Random_Start(), Border_Wraparound(), color =(100, 0, 0)), 
                    lambda screen: Unit(screen, Position_Center_Start(), Border_Bounce(), color =(0, 0, 255)),
                    lambda screen: Unit(screen, Position_Center_Start(), Border_Wraparound(), color =(0, 0, 100))
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

        # move and plot each unit
        for unit in units:
            unit.step(screen)
            unit.plot(screen)
            
        pygame.display.flip()  # update the screen
        pygame.time.Clock().tick(FRAMES_PER_SECOND) # limit frame rate


class Position_Strategy(ABC):
    @abstractmethod
    def init_position(self, unit, screen):
        """ Initialize position of a unit """
        ...

class Border_Strategy(ABC):
    @abstractmethod
    def handle_border(self, unit, screen):
        """ Handle a unit's movement at the edges of the screen. """
        ...

class Position_Random_Start(Position_Strategy):
    def init_position(self, unit, screen):
        pass

class Position_Center_Start(Position_Strategy):
    def init_position(self, unit, screen):
        pass

class Border_Bounce(Border_Strategy):
    def handle_border(self, unit, screen):
        pass

class Border_Wraparound(Border_Strategy):
    def handle_border(self, unit, screen):
        pass

class Unit():

    def __init__(self, screen, position_strategy, border_strategy, color=(0, 255, 0)):
        """ Initialize a unit """
        maxspeed = 5
        self.dx = random.random() * maxspeed * 2 - maxspeed
        self.dy = random.random() * maxspeed * 2 - maxspeed
        self.color = color
        self.radius = 10

    def plot(self, screen):
        """ Plot a unit """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

    def step(self, screen):
        """ Take a step: move and possibly other actions. """
        self.move(screen)

    def move(self, screen):
        """ Move a unit """
        self.x += self.dx
        self.y += self.dy

if __name__ == "__main__":
    main()
