# Resolves vertical collisions between two rectangular objects
def resolve_y_collision(object, wall):
    # Downward collision detection
    if wall.is_collidable and wall.position[1] < object.position[1] + object.height and wall.position[1] > object.position[1]:
        object.position[1] = wall.position[1] - object.height
        object.is_touching_ground = True

    # Upwards collision detection
    if wall.is_collidable and object.position[1] < wall.position[1] + wall.height and object.position[1] + object.height > wall.position[1] + wall.height:
        object.position[1] = wall.position[1] + wall.height
