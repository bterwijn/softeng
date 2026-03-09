import pygame
import numpy as np

def make_transform(x=0, y=0, angle=0):
    """Create a 3x3 homogeneous transformation matrix from position and angle (degrees)."""
    rad = np.radians(angle)
    cos_a, sin_a = np.cos(rad), np.sin(rad)
    return np.array([
        [cos_a, -sin_a, x],
        [sin_a,  cos_a, y],
        [0,      0,     1]
    ], dtype=float)

def get_position(transform):
    """Extract position (x, y) from a 3x3 transform matrix."""
    return transform[0, 2], transform[1, 2]

def set_position(transform, x, y):
    """Set position in a 3x3 transform matrix."""
    transform[0, 2] = x
    transform[1, 2] = y

class Player:
    Rotate_Left = None
    Rotate_Right = None

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        self.transform = make_transform(width // 2, height // 2, 0)
        self.speed = pygame.Vector2(0, 0)
        self.radius = 20
        self.line_width = 4
        self.color = (255, 255, 255)
        rotation_angles = 5
        Player.Rotate_Left = make_transform(angle=-rotation_angles)
        Player.Rotate_Right = make_transform(angle=rotation_angles)
    
    def move(self, keys):
        """ 
        Moves the player by changing its speed based on keyboard 'keys' pressed. 
        Limits the speed by multipling it by '0.95'.
        """
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.transform @=  Player.Rotate_Left   # matrix multiplication
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.transform @=  Player.Rotate_Right  # matrix multiplication
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            acceleration = np.array([0.5, 0, 0])
            self.speed += pygame.Vector2(*(self.transform @ acceleration)[:2])
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            acceleration = np.array([-0.5, 0, 0])
            self.speed += pygame.Vector2(*(self.transform @ acceleration)[:2])

        self.speed *= 0.97

    def step(self, size):
        """ Changes the position of player based on its speed. """
        # Apply speed as translation
        translation = make_transform(self.speed.x, self.speed.y, 0)
        self.transform = translation @ self.transform
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Keeps the player on the window. """
        width, height = size
        x, y = get_position(self.transform)
        
        if x < self.radius:
            set_position(self.transform, self.radius, y)
            self.speed.x = -self.speed.x
            x = self.radius
        if y < self.radius:
            set_position(self.transform, x, self.radius)
            self.speed.y = -self.speed.y
            y = self.radius
        if x > width - self.radius:
            set_position(self.transform, width - self.radius, y)
            self.speed.x = -self.speed.x
            x = width - self.radius
        if y > height - self.radius:
            set_position(self.transform, x, height - self.radius)
            self.speed.y = -self.speed.y

    def draw(self, surface):
        """ Draw cicrle and direction line on the 'surface'. """
        position = pygame.Vector2(*get_position(self.transform))
        pygame.draw.circle(surface, self.color, position, self.radius, self.line_width)
        direction = np.array([self.radius * 3 / 2, 0, 0])
        dirvec = pygame.Vector2(*(self.transform @ direction)[:2])
        pygame.draw.line(surface, self.color, position, position + dirvec, self.line_width)
        
def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('steering')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    player = Player(surface.get_size())

    units = []
    units.append(player)

    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        for unit in units:
            unit.step(surface.get_size())
            unit.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
