class Point2D:
    def __init__(self, x=0, y=0): #define initializes a new point 2D
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})" 
#__str__ to make it easy to appear in coordinates

    def add(self, p):
        self.x += p.x
        self.y += p.y
#adds the coordinates of p2 in this examble to the current point p1

    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5
        return dist
#to calc the distance according to the distance law

p1 = Point2D(1, 2) #Define the first point
p2 = Point2D(4, -2) #Define the second point

p2.add(p1) #add point 2 to point 1

print(p2) # because of __str__ it wall appear (5,0)
print(p1.distance(p2)) #according to distance law it will be 4,7213595499958