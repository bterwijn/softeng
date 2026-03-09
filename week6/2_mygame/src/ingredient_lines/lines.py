import pygame
import copy
import random
import pymunk

# Global pymunk space for collision detection
space = pymunk.Space()

class Line:
    
    def __init__(self, start_pos, end_pos, color=(255, 255, 255), line_width=4):
        self.start_pos = pygame.Vector2(start_pos)
        self.end_pos = pygame.Vector2(end_pos)
        self.color = color
        self.line_width = line_width
        self.segment = None  # pymunk segment

    def draw(self, postion, surface):
        pygame.draw.line(surface, self.color, postion+self.start_pos, postion+self.end_pos, self.line_width)

    def create_segment(self, body):
        """Create a pymunk segment attached to the given body."""
        self.segment = pymunk.Segment(body, tuple(self.start_pos), tuple(self.end_pos), self.line_width / 2)
        return self.segment

class Static_Unit:
    
    def __init__(self):
        self.lines = []
        self.position = pygame.Vector2(0, 0)
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        space.add(self.body)

    def add_line(self, line):
        self.lines.append(line)
        segment = line.create_segment(self.body)
        segment.unit = self  # back-reference for collision detection
        space.add(segment)
        self._update_body_position()

    def _update_body_position(self):
        """Update the pymunk body position to match self.position."""
        self.body.position = (self.position.x, self.position.y)

    def step(self, units):
        return 

    def draw(self, surface):
        for line in self.lines:
            line.draw(self.position, surface)

    def if_collision(self, units):
        return False

class Unit(Static_Unit):

    def __init__(self, position):
        super().__init__()
        self.spwan = position
        self.body.body_type = pymunk.Body.KINEMATIC
        self.respawn()

    def respawn(self):
        self.position = copy.copy(self.spwan)
        dx, dy = 1+random.uniform(0, 2), 1+random.uniform(0, 2)
        if (random.choice([True, False])):
            dx = -dx
        if (random.choice([True, False])):
            dy = -dy
        self.speed = pygame.Vector2(dx, dy)
        self._update_body_position()

    def step(self, units):
        self.position += self.speed
        self._update_body_position()
        if self.if_collision(units):
            self.respawn()

    def if_collision(self, units):
        """Check if any of this unit's segments collide with other units' segments."""
        for line in self.lines:
            if line.segment is None:
                continue
            shape_filter = pymunk.ShapeFilter()
            for contact in space.shape_query(line.segment):
                other_shape = contact.shape
                if hasattr(other_shape, 'unit') and other_shape.unit is not self:
                    return True
        return False


def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('lines')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)
    
    environment = Static_Unit()
    p1 = (100 + random.randint(-50, 50), 100 + random.randint(-50, 50))
    p2 = (700 + random.randint(-50, 50), 100 + random.randint(-50, 50))
    p3 = (700 + random.randint(-50, 50), 500 + random.randint(-50, 50))
    p4 = (100 + random.randint(-50, 50), 500 + random.randint(-50, 50))
    environment.add_line(Line(p1, p2))
    environment.add_line(Line(p2, p3))
    environment.add_line(Line(p3, p4))
    environment.add_line(Line(p4, p1))

    player = Unit(pygame.Vector2(400,300))
    # triangle
    player.add_line(Line(( -20,  20), (  20,  20)))  # base
    player.add_line(Line((  20,  20), (   0, -20)))  # right side
    player.add_line(Line((   0, -20), ( -20,  20)))  # left side

    units = [environment, player]
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        surface = pygame.display.get_surface()
        for player in units:
            player.step(units)
            player.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
