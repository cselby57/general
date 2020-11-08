from dataclasses import dataclass
import math


# geometry ref: http://paulbourke.net/geometry/pointlineplane/
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
        self.eq = None

    def define(self, v0: Vector3, v1: Vector3):
        self.vertex0 = v0
        self.vertex1 = v1

    def is_on(self, v: Vector3):
        tol = 0.000001
        if self.vertex1 and self.vertex0:
            # check if the reference point is on the line equation

            # check for possible 0 division errors on each axis and handle
            if abs(self.vertex1.X - self.vertex0.X) < tol:
                if abs(v.X - self.vertex0.X) > tol:
                    return False
                else:
                    dx = tol
            else:
                dx = (self.vertex1.X - self.vertex0.X)

            if abs(self.vertex1.Y - self.vertex0.Y) < tol:
                if abs(v.Y - self.vertex0.Y) > tol:
                    return False
                else:
                    dy = tol
            else:
                dy = (self.vertex1.Y - self.vertex0.Y)

            if abs(self.vertex1.Z - self.vertex0.Z) < tol:
                if abs(v.Z - self.vertex0.Z) > tol:
                    return False
                else:
                    dz = tol
            else:
                dz = (self.vertex1.Z - self.vertex0.Z)

            rx = (v.X - self.vertex0.X) / dx
            ry = (v.Y - self.vertex0.Y) / dy
            rz = (v.Z - self.vertex0.Z) / dz
            if abs(rx - ry) < tol and abs(rx - rz) < tol and abs(ry - rz) < tol:
                # now check that the point is within the bounds of the end points
                if v.X >= min(self.vertex0.X, self.vertex1.X) or v.X <= max(self.vertex0.X, self.vertex1.X) or\
                        v.Y >= min(self.vertex0.Y, self.vertex1.Y) or v.Y <= max(self.vertex0.Y, self.vertex1.X) or\
                        v.Z >= min(self.vertex0.Z, self.vertex1.Z) or v.Z <= max(self.vertex0.Z, self.vertex1.X):
                    return True

        return False

    def intersects(self, point: Vector3, dir_vector: Vector3):
        # determine if a given line segment intersects the edge
        # assign aliases
        a = self.vertex0
        b = self.vertex1
        c = point
        d = dir_vector
        tol = 0.000001

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
        if int_distance < tol:
            # now check if the first intersection point (collinear to the edge) is inside the bounds of the edge
            if self.is_on(pab):
                # if so then returh true
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
            if v is Vector3:
                self.vertices.append(v)
        self.degree = len(self.vertices)
        if self.degree == len(vertex_list) and self.degree > 2:
            # confirm all items in vertex_list were added and that at least 3 points were added
            # solve plane equation using first 3 points
            self.plane.eq_from_3_points(self.vertices[0], self.vertices[1], self.vertices[2])
            for vv in self.vertices:
                if not self.plane.is_on(vv):
                    # if any point in the vertex list is not planar with the others return false
                    self.vertices = []
                    self.degree = 0
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
            self.edges.append(e.define(self.vertices[i], self.vertices[i+1]))

        # last edge is always vertex[-1] to vertex[0]
        e = Edge()
        self.edges.append(e.define(self.vertices[-1], self.vertices[0]))

    def is_inside(self, p: Vector3):
        # determine if the point is inside of the polygon
        tol = 0.000001
        # confirm the point is on the plane of the polygon
        if not self.plane.is_on(p):
            return False
        # create a ray that is on the plane
        normal = Vector3(X=self.plane.eq.A, Y=self.plane.eq.B, Z=self.plane.eq.C)
        return


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
        tol = .0000001
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








