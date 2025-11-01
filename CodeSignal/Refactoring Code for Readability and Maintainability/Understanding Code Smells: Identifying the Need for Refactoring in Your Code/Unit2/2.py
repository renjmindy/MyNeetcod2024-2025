def calculate_and_print(points):
    for point in points:
        distance = distance_between_two_points(point)
        print(f"Distance of Point({point['x']}, {point['y']}) from origin is {distance:.2f}")

def distance_between_two_points(point):
    return (((point['x'] - 0)**2 + (point['y'] - 0)**2)**0.5)
    

points = [{'x': 3, 'y': 4}, {'x': 5, 'y': 12}, {'x': 8, 'y': 15}]
calculate_and_print(points)
