def largestTriangleArea(points):
    width_max = max(point[0] for point in points)
    hight_max = max(point[1] for point in points)
    width_min = min(point[0] for point in points)
    hight_min = min(point[1] for point in points)
    return 

points = [[4,6],[6,5],[3,1]]
print(largestTriangleArea(points))