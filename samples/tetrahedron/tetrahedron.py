import pascale
import math
from math import sqrt
import aerion_tools 

# create geometry using the paradigm: pascale.category.What.how

# create a tetrahedral object with cylindrical "edges" and 
# riangular links to the center point

# function to create edges between vertices fo tetrahedron
def make_edges(edge_list,link_list,current_link):
    if(4 == current_link):
        # cant have an edge from vertex to itself; finished
        return edge_list
    else:
        # if vertices remain to be connected, connect them to the current link
        for i in range (current_link+1,len(link_list)):
            edge_list.append(pascale.curve.Line.from_end_points(link_list
                             [current_link].end,link_list[i].end))
    # once edges have been made to this link / vertex do so for remaining links
    return make_edges(edge_list,link_list,current_link+1)

# function to make a list of points repesenting an equilateral triangle in x-y plane
# about origin
# in hindsight could have made a triangle class with rotation function
# to be cleaner, but almost done with script
def triangle(edge_length):
    # create a point and then rotate copies to make triangle
    vertex1 = pascale.Point3D(edge_length*sqrt(3)/3,0,0)
    vertex2 = vertex1.copy()
    vertex2.rotate((0,0,1),120,True)
    vertex3 = vertex2.copy()
    vertex3.rotate((0,0,1),120,True)
    return [vertex1, vertex2, vertex3]

# function to rotate a triangle
def rot_triangle(tri,axis,angle,deg):
    # make a copy for convenience
    triR = [tri[0].copy(), tri[1].copy(), tri[2].copy()]
    for i in range(3):
        triR[i].rotate(axis,angle,deg)
    return triR

    

### begin main script

# basic parameters
center_dist = 2   # distance from vertex to origin
phi = 109.4712    # "tetrahedral angle" - angle from vertex1 to center to vertex 2 
phi_rad = 1.9106  # phi in radians
edge_radius = .15 # radius of cyclinders comprising edges
link_side_length = .2 # side length of triangular links

# begin by creating centerlines for each link and edge, and triangular profile for
# links
links = []
edges = []
triangles = []
# location of first vertex, aligned with z axis and origin
cur_vertex = pascale.Point3D(0,0,center_dist)
# create first link
links.append(pascale.curve.Line.from_end_points(pascale.ORIGIN,cur_vertex)) 
cur_vertex.rotate((0,1,0),phi,True) # rotate to update vertex

# also create triangles centered around each link
cur_tri = triangle(link_side_length)
triangles.append(cur_tri)
cur_tri = rot_triangle(cur_tri,(0,0,1),180,True) # flip around z so edges align nicely
cur_tri = rot_triangle(cur_tri,(0,1,0),phi,True)

# rotate 120 about z to create remaining vertices
for i in range(0,3):
    # add the next vertex link
    links.append(pascale.curve.Line.from_end_points(pascale.ORIGIN,cur_vertex))
    # add the next triangle
    triangles.append(cur_tri)
    # update vertex by rotating 120 degrees
    cur_vertex.rotate((0,0,1),120,True) 
    cur_tri = rot_triangle(cur_tri,(0,0,1),120,True)

# now connect vertices lines to form edges
edges = make_edges(edges,links,0)   

# now that reference geometries are created we can create bodies

# start with spehere at origin
tetra = pascale.body.Sphere.from_center_radius(pascale.ORIGIN,edge_radius*2) 
# add cylinders for edges first
for i in range(len(edges)):
    # add a cyclnder for each edge to the tetrahedral body
    tetra += pascale.body.Cylinder.from_centers_radius(edges[i].start,edges[i].end,
                                                       edge_radius)
    
# now add triangle inner links, and spheres to cap vertices
print(len(triangles))
for i in range(len(links)):
    # create a polyline for each triangular profile
    profile = pascale.curve.PolyLine.from_points(triangles[i],True)
    # extrude the profile
    tetra += pascale.body.Extrude.profile_along_direction(profile,links[i].direction,
                                                          center_dist)
    # add sphere to cap ends
    tetra += pascale.body.Sphere.from_center_radius(links[i].end,edge_radius)


# pass geometric entities to display
aerion_tools.viewer.show(tetra)



