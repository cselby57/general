from dataclasses import dataclass
import math


# geometry ref: http://paulbourke.net/geometry/pointlineplane/

tol = .000000001

@dataclass
class Vector3:
    # hold 3 floats to describe a vector or point
    X: float
    Y: float
    Z: float

    def __add__(self, other):
        new_x = self.X + other.X
        new_y = self.Y + other.Y
        new_z = self.Z + other.Z
        new_vector3 = Vector3(X=new_x, Y=new_y, Z=new_z)
        return new_vector3

    def __sub__(self, other):
        new_x = self.X - other.X
        new_y = self.Y - other.Y
        new_z = self.Z - other.Z
        new_vector3 = Vector3(X=new_x, Y=new_y, Z=new_z)
        return new_vector3

    def __mul__(self, scalar: float):
        new_x = self.X * scalar
        new_y = self.Y * scalar
        new_z = self.Z * scalar
        new_vector3 = Vector3(X=new_x, Y=new_y, Z=new_z)
        return new_vector3

    def __eq__(self, other):
        dx = abs(self.X - other.X)
        dy = abs(self.Y - other.Y)
        dz = abs(self.Z - other.Z)
        if dx + dy + dz <= tol:
            return True
        else:
            return False

    def get_perpendicular(self):
        if self.Y == 0 and self.Z == 0:
            if self.X == 0:
                raise ValueError('zero vector')
            else:
                cross_v = Vector3(X=0, Y=1, Z=0)
        else:
            cross_v = Vector3(X=1, Y=0, Z=0)

        ret = self.cross_v3(self, cross_v)
        return ret

    @staticmethod
    def cross_v3(v0, v1):
        # cross product of 2 3 dimensional vectors
        x = (v0.Y * v1.Z) - (v0.Z * v1.Y)
        y = (v0.X * v1.Z) - (v0.Z * v1.X)
        z = (v0.X * v1.Y) - (v0.Y * v1.X)
        return Vector3(x, y, z)

    def magnitude(self):
        ret = math.sqrt((self.X ** 2) + (self.Y ** 2) + (self. Y ** 2))
        return ret


@dataclass
class PlaneEQ:
    A: float
    B: float
    C: float
    D: float


class Edge:

    def __init__(self):
        self.vertex0 = None
        self.vertex1 = None
        self.eq = []

    def define(self, v0: Vector3, v1: Vector3):
        self.vertex0 = v0
        self.vertex1 = v1

    def is_on(self, v: Vector3):
        if self.vertex1 and self.vertex0:
            # check if the reference point is on the line equation
            # check for possible 0 division errors if the edge points align with a coordinate axis
            rx_flag = True
            if abs(self.vertex1.X - self.vertex0.X) < tol:
                # if the edge points have the same x but the reference point does not they are not collinear
                if abs(v.X - self.vertex0.X) > tol:
                    return False
                else:
                    rx_flag = False # skip collinear check, the reference point is already collinear
            else:
                dx = (self.vertex1.X - self.vertex0.X)

            if abs(self.vertex1.Y - self.vertex0.Y) < tol:
                if abs(v.Y - self.vertex0.Y) > tol:
                    return False
                else:
                    rx_flag = False
            else:
                dy = (self.vertex1.Y - self.vertex0.Y)

            if abs(self.vertex1.Z - self.vertex0.Z) < tol:
                if abs(v.Z - self.vertex0.Z) > tol:
                    return False
                else:
                    rx_flag = False
            else:
                dz = (self.vertex1.Z - self.vertex0.Z)

            if rx_flag:
                # check for collinearity
                rx = (v.X - self.vertex0.X) / dx
                ry = (v.Y - self.vertex0.Y) / dy
                rz = (v.Z - self.vertex0.Z) / dz
                if not abs(rx - ry) < tol and not abs(rx - rz) < tol and not abs(ry - rz) < tol:
                    # point is not so not on the edge either collinear
                    return False

            # point is collinear if here
            # now check that the point is within the bounds of the end points
            if v.X >= min(self.vertex0.X, self.vertex1.X) and v.X <= max(self.vertex0.X, self.vertex1.X) and\
                    v.Y >= min(self.vertex0.Y, self.vertex1.Y) and v.Y <= max(self.vertex0.Y, self.vertex1.Y) and\
                    v.Z >= min(self.vertex0.Z, self.vertex1.Z) and v.Z <= max(self.vertex0.Z, self.vertex1.Z):
                return 'on_edge'
            else:
                return 'collinear'

        return False

    def intersects(self, point: Vector3, dir_vector: Vector3):
        # determine if a given line segment intersects the edge
        # assign aliases
        a = self.vertex0
        b = self.vertex1
        c = point
        d = point + (dir_vector * 100000)  # far away in 1 direction

        # expanded dot products
        Dacdc = self.Dmnop(a, c, d, c)
        Ddcba = self.Dmnop(d, c, b, a)
        Dacba = self.Dmnop(a, c, b, a)
        Ddcdc = self.Dmnop(d, c, d, c)
        Dbaba = self.Dmnop(b, a, b, a)

        # mu coefficients
        mua = ((Dacdc * Ddcba) - (Dacba * Ddcdc)) / ((Dbaba * Ddcdc) * (Ddcba * Ddcba))
        mub = (Dacdc + (mua * Ddcba)) / Ddcdc

        # solve for points of shortest line segment connecting reference lines
        pab = a + ((b - a) * mua)
        pcd = c + ((d - c) * mub)

        # if the length of the shortest lien segment is less than tol, the points are the "same" point
        # and the lines intersect
        int_distance = self.length(pab, pcd)

        #print(int_distance)
        if int_distance < tol:
            # now check if the first intersection point (collinear to the edge) is inside the bounds of the edge
            # make an edge from the reference point and arbitrary rar point in the plane to check direction
            temp_edge = Edge()
            temp_edge.define(c, d)
            if self.is_on(pab) and temp_edge.is_on(pcd):
                # if so then return true
                return True

        return False

    def Dmnop(self, m: Vector3, n: Vector3, o: Vector3, p: Vector3):
        # helper for intersects function
        ret = ((m.X - n.X) * (o.X - p.X)) + ((m.Y - n.Y) * (o.Y - p.Y)) + ((m.Z - n.Z) * (o.Z - p.Z))
        return ret

    @staticmethod
    def length(v0: Vector3, v1: Vector3):
        # length of line segment between given points
        ret = math.sqrt(((v1.X - v0.X) ** 2) + ((v1.Y - v0.Y) ** 2) + ((v1.Z - v0.Z) ** 2))
        return ret
    
    @staticmethod
    def are_parallel(v0: Vector3, v1: Vector3):
        # check for parallelism
        ab = b - a  # ab direction vector
        if v0.X == 0
            if abs((ab.X / dir_vector.X) - (ab.Y / dir_vector.Y)) < tol and abs(
                    (ab.X / dir_vector.X) - (ab.Z / dir_vector.Z)) < tol \
                    and abs((ab.Z / dir_vector.Z) - (ab.Y / dir_vector.Y)) < tol:
                # lines are parallel so do not intersect
                return False

class Polygon:

    def __init__(self, color: str, texture: str):
        self.vertices = []
        self.degree = 0
        self.edges = []
        self.plane = Plane()
        self.color = color
        self.texture = texture

    def define_vertices(self, vertex_list):
        for v in vertex_list:
            # only add items if they are points
            if isinstance(v, Vector3):
                self.vertices.append(v)
        self.degree = len(self.vertices)
        # print(self.degree)
        if self.degree == len(vertex_list) and self.degree > 2:
            # confirm all items in vertex_list were added and that at least 3 points were added
            # solve plane equation using first 3 points
            self.plane.eq_from_3_points(self.vertices[0], self.vertices[1], self.vertices[2])
            for vv in self.vertices:
                if not self.plane.is_on(vv):
                    # if any point in the vertex list is not planar with the others return false
                    self.vertices = []
                    self.degree = 0
                    # print('a point is not planar')
                    return False
            return True

        # if an improper vertex list is found reset instance vars to default/empty
        self.vertices = []
        self.degree = 0
        return False

    def define_edges(self):
        # use the points in vertex list to define edges, must have at least 3 points to make 3 edge closed polygon
        if self.degree < 2 or self.vertices == []:
            return False

        for i in range(self.degree - 1):
            e = Edge()
            e.define(self.vertices[i], self.vertices[i + 1])
            # print(e)
            self.edges.append(e)

        # last edge is always vertex[-1] to vertex[0]
        e = Edge()
        e.define(self.vertices[-1], self.vertices[0])
        self.edges.append(e)
        return True

    def is_inside(self, p: Vector3):
        if not self.edges:
            return False
        # determine if the point is inside of the polygon
        # confirm the point is on the plane of the polygon
        if not self.plane.is_on(p):
            return False
        # check if the point on a vertex, easy find
        for v in self.vertices:
            if v == p:
                return True
        # create a ray that is on the plane
        normal = Vector3(X=self.plane.eq.A, Y=self.plane.eq.B, Z=self.plane.eq.C)
        ray = normal.get_perpendicular()

        # project the ray from the starting point and count how many edges it intersects
        count = 0
        for e in self.edges:
            on_edge = e.is_on(p)
            if on_edge == 'on_edge':
                # first check if the point is just on the line
                return True
            elif on_edge == 'collinear':
                # the point is collinear to and edge, but not within the bound so it is outside the polygon
                return False
            if e.intersects(p, ray):
                count += 1

        if count % 2 == 1:
            return True
        else:
            return False


class Plane:

    def __init__(self):
        self.eq = None

    def eq_from_3_points(self, v0: Vector3, v1: Vector3, v2: Vector3):
        # construct 2 vectors using v0 as the intersection
        vector0 = Vector3(X=v1.X - v0.X, Y=v1.Y - v0.Y, Z=v1.Z - v2.Z)
        vector1 = Vector3(X=v2.X - v0.X, Y=v2.Y - v0.Y, Z=v2.Z - v2.Z)

        # take the cross product to get A, B, C coefficients
        cross_product = Vector3.cross_v3(vector0, vector1)
        a = cross_product.X
        b = cross_product.Y
        c = cross_product.Z

        # solve for D using v0 as point on the plane
        d = (a * v0.X) + (b * v0.Y) + (c * v0.Z)

        # save coefficients to object
        self.eq = PlaneEQ(A=a, B=b, C=c, D=d)

    def is_on(self, v: Vector3):
        # use plane equation to determine if a given point is on the plane
        cofs = self.eq

        d = (cofs.A * v.X) + (cofs.B * v.Y) + (cofs.C * v.Z)
        if abs(cofs.D - d) <= tol:
            return True
        else:
            return False

    def find_intersection_point(self, p0: Vector3, p1: Vector3):
        # given 2 points to represent a line, find the point on the plane and in the line
        num = (self.eq.A * p0.X) + (self.eq.B * p0.Y) + (self.eq.C * p0.Z) + self.eq.D
        den = (self.eq.A * (p0.X - p1.X)) + (self.eq.B * (p0.Y - p1.Y)) + (self.eq.C * (p0.Z - p1.Z))
        if den == 0:
            return False
        u = num / den

        int_point = p0 + ((p1 - p0) * u)
        return int_point








