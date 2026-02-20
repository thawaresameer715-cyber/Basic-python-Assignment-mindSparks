#19. Tuple unpacking: Loop over list of (x,y) coords, dict to count quadrant (if x>0,y>0 etc.).
coords = [(1, 2), (-3, 4), (-5, -2), (8, -1), (0, 5), (2, 2), (-1, -1)]

quadrant_counts = {
    "Quadrant 1": 0,
    "Quadrant 2": 0,
    "Quadrant 3": 0,
    "Quadrant 4": 0,
    "Axis/Origin": 0
}

for x, y in coords:
    if x > 0 and y > 0:
        quadrant_counts["Quadrant 1"] += 1
    elif x < 0 and y > 0:
        quadrant_counts["Quadrant 2"] += 1
    elif x < 0 and y < 0:
        quadrant_counts["Quadrant 3"] += 1
    elif x > 0 and y < 0:
        quadrant_counts["Quadrant 4"] += 1
    else:
        quadrant_counts["Axis/Origin"] += 1

for quad, count in quadrant_counts.items():
    print(f"{quad}: {count}")