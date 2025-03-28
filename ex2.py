x_coor = [1, 2, 3, 4, 5]
y_coor = [2, 4, 6, 8, 10]
z_coor = [0, -1, -2, -3, -4]

points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]

#[(1, 2, 0), (2, 4, -1), (3, 6, -2), (4, 8, -3), (5, 10, -4)]

#The zip() function is used to combine multiple iterable objects into tuples
#It stops combining as soon as the shortest iterable is exhausted