import random

def generate_random_list(shape):
    """
    Generate a list of lists with random values based on the given shape.

    :param shape: A tuple (rows, columns) representing the shape of the list to be generated.
    :return: A list of lists with random values, matching the provided shape.
    """
    num_rows, num_cols = shape
    return [[random.random() for _ in range(num_cols)] for _ in range(num_rows)]

# Example usage:
random_list = generate_random_list((3, 2))
print(random_list)