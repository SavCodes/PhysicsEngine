import numpy as np
import pygame

class Object:
    def __init__(self, x, y, width, height, color="red"):
        self.position = np.array([x, y])
        self.velocity = np.array([0, 0])
        self.acceleration = np.array([0, 0])
        self.color = color
        self.width = width
        self.height = height
        self.is_collidable = True

    def display(self, screen):
        # Draw object to the screen
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))

    def update_position(self):
        x, y = pygame.mouse.get_pos()
        self.position  = np.array([x, y])


def resolve_x_collision(object, wall):
    # Right-sided collision detection
    if wall.is_collidable and wall.position[0] < object.position[0] + object.width and wall.position[0] > object.position[0]:
        object.position[0] = wall.position[0] - object.width
        object.is_touching_ground = True

    # Left-sided collision detection
    if wall.is_collidable and object.position[0] < wall.position[0] + wall.width and object.position[0] + object.width > wall.position[0] + wall.width:
        object.position[0] = wall.position[0] + wall.width

def event_checker():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True

def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    return screen, clock

def main():
    running = True
    screen, clock = initialize_pygame()

    test_object = Object(screen.width // 2, screen.height // 2, 80, 30, color="green")

    collidables = {
        "left_wall":  Object(0, 0, 50, screen.height, color="blue"),
        "right_wall": Object(screen.width-50, 0, 50, screen.height, color="red")
    }

    while running:
        running = event_checker()
        screen.fill((0,0,0))

        # Display the test object and update its position
        test_object.display(screen)
        test_object.update_position()

        # Loop through objects and resolve collisions
        for name, collidable in collidables.items():
            resolve_x_collision(test_object, collidable)
            collidable.display(screen)

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
