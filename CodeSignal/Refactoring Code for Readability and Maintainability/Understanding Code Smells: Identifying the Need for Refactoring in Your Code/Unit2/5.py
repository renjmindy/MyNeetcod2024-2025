# Combined function with unclear variable names and dual functionality
def calculate_properties(dim1, dim2):
    perimeter = 2 * (dim1 + dim2)
    area = dim1 * dim2
    return perimeter, area

def calculate_perimeter(dim1, dim2): return 2 * (dim1 + dim2)

def calculate_area(dim1, dim2): return dim1 * dim2

# Function to print the geometry of a "rectangle" with generic terms.
def print_properties(length, width):
    #perimeter, area = calculate_properties(length, width)
    perimeter, area = calculate_perimeter(length, width), calculate_area(length, width)
    print(f"Shape with dimension 1: {length} and dimension 2: {width} has:")
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")

# Constants for the dimensions of the shape.
SHAPE_DIM1 = 10
SHAPE_DIM2 = 5

print_properties(SHAPE_DIM1, SHAPE_DIM2)
