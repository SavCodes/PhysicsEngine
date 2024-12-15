# Resolves vertical collisions between two rectangular objects
def resolve_y_collision(object, wall):
    # Downward collision detection
    if wall.is_collidable and wall.position[1] < object.position[1] + object.height and wall.position[1] > object.position[1]:
        object.position[1] = wall.position[1] - object.height
        object.is_touching_ground = True

    # Upwards collision detection
    if wall.is_collidable and object.position[1] < wall.position[1] + wall.height and object.position[1] + object.height > wall.position[1] + wall.height:
        object.position[1] = wall.position[1] + wall.height

# Resolves horizontal collisions between two rectangular objects
def resolve_x_collision(object, wall):
    # Right-sided collision detection
    if wall.is_collidable and wall.position[0] < object.position[0] + object.width and wall.position[0] > object.position[0]:
        object.position[0] = wall.position[0] - object.width
        object.is_touching_ground = True

    # Left-sided collision detection
    if wall.is_collidable and object.position[0] < wall.position[0] + wall.width and object.position[0] + object.width > wall.position[0] + wall.width:
        object.position[0] = wall.position[0] + wall.width
