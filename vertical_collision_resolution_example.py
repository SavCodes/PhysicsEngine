import numpy as np
import pygame

# Example object to prove vertical collision resolving
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

def resolve_y_collision(object, wall):
    # Downward collision detection
    if wall.is_collidable and wall.position[1] < object.position[1] + object.height and wall.position[1] > object.position[1]:
        object.position[1] = wall.position[1] - object.height
        object.is_touching_ground = True

    # Upwards collision detection
    if wall.is_collidable and object.position[1] < wall.position[1] + wall.height and object.position[1] + object.height > wall.position[1] + wall.height:
        object.position[1] = wall.position[1] + wall.height

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

    test_object = Object(screen.width // 2, screen.height // 2, 30, 80, color="green")

    collidables = {
        "floor":  Object(0, screen.height - 50, screen.width, 50, color="blue"),
        "ceiling": Object(0, 0, screen.width, 50, color="red")
    }

    while running:
        running = event_checker()
        screen.fill((0,0,0))

        # Display the test object and update its position
        test_object.display(screen)
        test_object.update_position()

        # Loop through objects and resolve collisions
        for name, collidable in collidables.items():
            resolve_y_collision(test_object, collidable)
            collidable.display(screen)

        # Update the display
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
