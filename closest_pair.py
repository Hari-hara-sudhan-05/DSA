class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def brute_force(points):
    min_dist = float('inf')
    min_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = (points[i], points[j])
    return min_dist, min_pair


def closest_strip(strip, min_dist):
    min_strip_dist = min_dist
    min_strip_pair = None
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < min_strip_dist:
                min_strip_dist = dist
                min_strip_pair = (strip[i], strip[j])
    return min_strip_dist, min_strip_pair


def closest_pair_util(points):
    if len(points) <= 3:
        return brute_force(points)
    
    mid = len(points) // 2
    mid_point = points[mid]
    left_dist, left_pair = closest_pair_util(points[:mid])
    right_dist, right_pair = closest_pair_util(points[mid:])
    
    min_dist, min_pair = min((left_dist, left_pair), (right_dist, right_pair))
    strip = []
    for point in points:
        if abs(point.x - mid_point.x) < min_dist:
            strip.append(point)
    
    strip_dist, strip_pair = closest_strip(strip, min_dist)
    
    if strip_dist < min_dist:
        min_dist = strip_dist
        min_pair = strip_pair
    
    return min_dist, min_pair


def closest_pair(points):
    points = sort_points(points)
    min_dist, min_pair = closest_pair_util(points)
    return min_dist, min_pair


def sort_points(points):
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i].x > points[j].x or (points[i].x == points[j].x and points[i].y > points[j].y):
                points[i], points[j] = points[j], points[i]
    
    return points


points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
min_dist, min_pair = closest_pair(points)
print(f'{min_dist}   min pair {min_pair[0].x, min_pair[0].y} {min_pair[1].x, min_pair[1].y}')