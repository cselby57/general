from polygon import *
import ansi_codes

a = Vector3(0,0,0)
b = Vector3(10,0,0)
c = Vector3(10,10,0)
d = Vector3(0,10,0)

points = [a, b, c, d]

square = Polygon(ansi_codes.blue, '@')
if square.define_vertices(points):
    print('\nSuccessfully added points to square')
    print(square.vertices)
    print(square.plane.eq)
if square.define_edges():
    print('Successfully defined the edges')
    print(repr(square.edges))

print('\n\n')
line = ''
for y in range(11, -2, -1):
    for x in range(-1, 12):
        if square.is_inside(Vector3(X=x, Y=y, Z=0)):
            line = line + 'Y'
        else:
            line = line + 'N'
    line = line + '\n'
line = square.color + line
print(line)