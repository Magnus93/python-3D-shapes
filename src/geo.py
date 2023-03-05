import pygame
import transform
import projection
from math import *
screen = pygame.display.set_mode((800 , 500))
pygame.font.init()
smallfont = pygame.font.SysFont("verdana", 14)

def sphere(t_seg = 30, h_seg=30, radius = 1.0):							# create sphere shape
    verts = []
    trigs = []
    h_angle = pi/h_seg
    t_angle = 2*pi/t_seg
    verts.append((radius,0,0)) 											# top vertex
    for h in range(1,h_seg):											# middle middle vertecies
        for t in range(0,t_seg):										# ---------||-----------
            vertex = transform.rot_z((radius,0,0),-h_angle*h)			# ---------||-----------
            vertex = transform.rot_x(vertex,t_angle*t)					# ---------||-----------
            verts.append(vertex)						
    for t in range(2,t_seg+2):											# bottom triangles
        if t > t_seg:													# -------||------
            trigs.append((0,t-1,1))										
        else:
            trigs.append((0,t-1,t))
			
    for h in range(1,h_seg-1):
        for t in range(1,t_seg+2):
            trigs.append(((h-1)*t_seg+t,h*t_seg+t-1, h*t_seg+t))
            trigs.append(((h-1)*t_seg+t,(h-1)*t_seg+t-1, h*t_seg+t-1))

    for t in range(2,t_seg+1):                                          # bottom triangles
        trigs.append((len(verts),(h_seg-2)*t_seg+t,(h_seg-2)*t_seg+t-1))

    verts.append((-radius,0,0))                                         # bottom vertex
    return shape(verts,trigs) 

def cube(w,h,d):
    polys = []
    verts = []
    (w,h,d) = (w/2,h/2,d/2)
    verts.append((-1*w,-1*h,-1*d))
    verts.append((-1*w,-1*h, 1*d))
    verts.append((-1*w, 1*h,-1*d))
    verts.append((-1*w, 1*h, 1*d))
    verts.append(( 1*w,-1*h,-1*d))
    verts.append(( 1*w,-1*h, 1*d))
    verts.append(( 1*w, 1*h,-1*d))
    verts.append(( 1*w, 1*h, 1*d))
    polys.append((0,1,2))
    polys.append((3,2,1))
    polys.append((5,4,6))
    polys.append((6,7,5))
    polys.append((1,0,4))
    polys.append((1,4,5))
    polys.append((1,5,3))
    polys.append((5,7,3))
    polys.append((2,3,7))
    polys.append((7,6,2))
    polys.append((0,6,4))
    polys.append((0,2,6))
    return shape(verts, polys)

def cylinder(seg = 10, height = 6, radius = 2):
    polys = []
    verts = []
    angle = 2*pi/seg
    verts.append((0,height/2,0))
    for i in range(seg):
        vertex = transform.rot_y((radius, height/2, 0), i*angle)
        verts.append((vertex))
    for i in range(seg):
        vertex = transform.rot_y((radius, -height/2, 0), i*angle)
        verts.append((vertex))
    verts.append((0,-height/2,0))
    
    for i in range(1,seg):
        polys.append((0,i,i+1))
    polys.append((0,i+1,1))
    for i in range(1,seg):
        polys.append((i+1, i, i+seg))
        polys.append((i+seg, i+seg+1, i+1))
    polys.append((1, seg, 2*seg))
    polys.append((2*seg, seg+1, 1))
    for i in range(1, seg):
        polys.append((2*seg+1, seg+i+1, seg+i))
    polys.append((2*seg+1, seg+1, 2*seg))
    return shape(verts, polys)
    
def torus(seg1 = 10, seg2 = 5,r1 = 3, r2 = 1):
    polys = []
    verts = []
    angle1 = 2.0*pi/seg1
    angle2 = 2.0*pi/seg2
    for i in range(seg2):
        vertex = ((0,0,r1+r2))
        vertex = transform.move(vertex, (0,0,-r1))
        vertex = transform.rot_x(vertex, i*angle2)
        vertex = transform.move(vertex, (0,0,r1))
        verts.append((vertex))
    for i in range(seg1-1):
        for j in range(seg2):
            vertex = transform.rot_y(verts[j],angle1*(i+1))
            verts.append((vertex))
    for i in range(seg1-1):
        offset = i*seg2
        for j in range(seg2-1):
            polys.append((i*seg2+j,i*seg2+j+1,i*seg2+j+seg2))
            polys.append((i*seg2+j+1,i*seg2+j+seg2+1,i*seg2+j+seg2))
        polys.append((i*seg2, (i+1)*seg2, (i+1)*seg2-1))
        polys.append(((i+1)*seg2-1,  (i+1)*seg2 , (i+2)*seg2-1))
    for i in range(seg2):
        if i < seg2-1:
            polys.append((i+1, i, i+(seg1-1)*seg2))
            polys.append((i+1, i+(seg1-1)*seg2, i+(seg1-1)*seg2+1))
        else:
            polys.append((0, seg2-1,len(verts)-1))
            polys.append((0, len(verts)-1, len(verts)-seg2))
    return shape(verts, polys)

def lathe(seg = 10, pos2D = [(0.1,4),(2,3),(2.5,1),(4,-1),(3.5,-2),(0.3,-4)]):
    seg2 = len(pos2D)
    polys = []
    verts = []
    angle = 2*pi/seg
    for i in range(seg2):
        print(i)
        verts.append((pos2D[i][0], pos2D[i][1], 0))
    for i in range(seg-1):
        for j in range(seg2):
            vertex = transform.rot_y(verts[j], angle*(i+1))
            verts.append((vertex))
    for i in range(seg-1):
        for j in range(seg2-1):
            polys.append((seg2*i+j, seg2*i+j+1   , seg2*i+j+seg2   ))
            polys.append((seg2*i+j+seg2, seg2*i+j+1, seg2*i+j+seg2+1))
    for i in range(seg2-1):
        polys.append((i+1, i, i+seg2*(seg-1)))
        polys.append((i+seg2*(seg-1),i+seg2*(seg-1)+1, i+1))
    return shape(verts, polys)

class shape:                            # shape class
    def __init__(self, verts, polys):
        self.verts = verts
        self.verts0 = verts
        self.verts2d = []
        self.proj2d()
        self.poly = polys
        if len(polys)>1:
            self.createLines()
        
    def createLines(self):
        self.line = [(self.poly[0][0], self.poly[0][1])]
        for i in (self.poly):
            if not self.line_exist((i[0],i[1])):
                self.line.append((i[0],i[1]))
            if not self.line_exist((i[1],i[2])):
                self.line.append((i[1],i[2]))
            if not self.line_exist((i[2],i[0])):
                self.line.append((i[2],i[0]))

       
    def line_exist(self, line):
        in_list = False
        for i in self.line:
            if (i[0] == line[0] and i[1] == line[1]):
                return True
            elif (i[0] == line[1] and i[1] == line[0]):
                return True
        return False
    
    def proj2d(self):
        self.verts2d = []
        for i in self.verts:
            self.verts2d.append(projection.projtype(i))

    def rot(self, pos_start, pos_stop):
        (x,y) = pos_start
        (x_stop, y_stop) = pos_stop 
        dr_c = 120
        if x_stop != 0 or y_stop != 0:
            self.verts0 = self.verts
        ls_po = []
        for i in self.verts0:
            ls_po.append(transform.rot_y(transform.rot_x(i,(y+0.0)/dr_c),(-x+0.0)/dr_c))
        self.verts = ls_po

    def scale(self, scale):
        ls_po = []
        for i in self.verts:
            ls_po.append(transform.scale(i, scale))
        self.verts = ls_po
        self.verts0 = ls_po

def origin_show(face=screen):
    vectX = (projection.projtype((0,0,0)), projection.projtype((5,0,0)))
    pygame.draw.line(face, (255,0,0), vectX[0], vectX[1])
    x = smallfont.render("X", 1, (255,0,0))
    face.blit(x, vectX[1])
    vectY = (projection.projtype((0,0,0)), projection.projtype((0,5,0)))
    pygame.draw.line(face, (0,255,0), vectY[0], vectY[1])
    y = smallfont.render("Y", 1, (0,255,0))
    face.blit(y, vectY[1])
    vectZ = (projection.projtype((0,0,0)), projection.projtype((0,0,5)))
    pygame.draw.line(face, (0,0,255), vectZ[0], vectZ[1])
    z = smallfont.render("Z", 1, (0,0,255))
    face.blit(z, vectZ[1])

TheObject = shape([(0,0,0),(1,0,0)],[])
TheObject = cylinder(40, 8, 5)                                 

if __name__ == "__main__":
    my_polys = [(0,1,2),(0,3,2),(1,0,2),(1,2,7)]
    myshape = shape([(0,0,0),(1,1,1),(3,4.0,5),(3.0,50,50)], my_polys)
    print(myshape.poly)
    print("the line", myshape.line)
    print(myshape.line_exist((0,1)))

