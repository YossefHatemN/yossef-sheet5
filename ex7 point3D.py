class Point3D:
    def __init__(self, x=0, y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})" 


    def add(self, p):
        self.x += p1.x
        self.y += p1.y
        self.z += p1.z
    
    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        delta_z = self.z - p.z
        dist = (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5
        return dist


p1 = Point3D(1, 2, 3) 
p2 = Point3D(4, -2 ,0)

p2.add(p1) 

print(p2) 
print(p1.distance(p2))
