import random
import pygame
import sys
from math import *
import projection
import cam
import vector 
screen = pygame.display.set_mode((800 , 600))
pygame.font.init()
smallfont = pygame.font.SysFont("verdana", 14)


class gradient:                           # create a gradient
    def __init__(self,colors):
        self.colors = colors 	# [(r,b,g)]
    
    def __str__(self):
        string = "Gradient object colors: \n	"
        string += str(self.colors)
        return string

    def rev(self):
        self.colors.reverse();
        
    def getColor(self,value): # value 0 to 1.0
        value = value - int(value)				# example: value = 3.76 -> value = 0.76
        section = 1.0/(len(self.colors) - 1)
        begIndex = int(floor(value/section))
        begColor = self.colors[begIndex]
        #print begIndex+1, value
        endColor = self.colors[begIndex+1]
        deltaR = endColor[0] - begColor[0]
        deltaG = endColor[1] - begColor[1]
        deltaB = endColor[2] - begColor[2]
        red 	= int(begColor[0] + deltaR*((value-begIndex*section)/section))
        green 	= int(begColor[1] + deltaG*((value-begIndex*section)/section))
        blue 	= int(begColor[2] + deltaB*((value-begIndex*section)/section))
        return (red,green,blue)
        
    def show(self, x=0 ,y=0):
        for i in range(0,200):
            color = self.getColor(i/100.0)
            pygame.draw.line(screen, color, (x+3*i,y), (x+3*i,y+80),3)

#-----------------------------premade gradients-------------------------
rainbow 	= gradient([(255,255,255),(255,0,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255),(255,255,255)])
rainbow.rev()
fire 		= gradient([(255,255,255),(255,30,0),(255,200,0),(255,255,0),(0,0,255),(0,0,0)])
water 		= gradient([(0,0,120),(0,180,255),(0,250,255)])
blackwhite 	= gradient([(0,0,0),(255,255,255)])
turquoise 	= gradient([(0,255,100),(0,255,255),(0,100,255),(0,255,255),(0,255,100)])
bluepurp = gradient([(0,0,255),(255,0,255),(0,0,255),(255,0,255),(0,0,255),(255,0,255),(0,0,255),(255,0,255),(0,0,255),(255,0,255)]) 
stripped = gradient([(0,0,0),(255,255,255),(0,0,0),(255,255,255),(0,0,0),(255,255,255),(0,0,0),(255,255,255),(0,0,0),(255,255,255)])	
clay = gradient([(255,255,255), (180,0,0), (255,100,100), (200,0,0), (200,0,0), (255,100,100)])
#--------------------------end of premade gradients---------------------

maingrad = rainbow

def drawLine(pos1, pos2, face = screen, color =(0,200,200)):
    pygame.draw.line(face, color, pos1, pos2)
    
def draw_points(obj, face = screen, grad = rainbow):
    j = 0
    for i in range(0,len(obj.verts2d)):
        color = grad.getColor(0.05*cam.dictance(obj.verts[i]))
        drawLine((obj.verts2d[i][0]-2,obj.verts2d[i][1]-2),(obj.verts2d[i][0]+2,obj.verts2d[i][1]+2), face, color)
        drawLine((obj.verts2d[i][0]-2,obj.verts2d[i][1]+2),(obj.verts2d[i][0]+2,obj.verts2d[i][1]-2), face, color)
        if point_index:
            render_index = smallfont.render(str(j),1, (230,230,230))     # upper value
            face.blit(render_index, obj.verts2d[i])
            j += 1

def shade(obj, face = screen, grad = rainbow):
    polys = sort_polys(obj)
    verts = obj.verts
    verts2d = obj.verts2d
    for p in polys:
        v0 = verts[p[0]]
        v1 = verts[p[1]]
        v2 = verts[p[2]]
        vect1 = vector.sub(v1, v0)
        vect2 = vector.sub(v2, v0)
        normal = vector.cross_prod(vect1, vect2)
        angle = vector.angle(normal, (0,0,1))
        if angle < 2*pi/3:
            px0 = verts2d[p[0]]
            px1 = verts2d[p[1]]
            px2 = verts2d[p[2]]
            color = grad.getColor(angle/pi)
            pygame.draw.polygon(face, color, [px0,px1,px2])

def wireframe_color(obj, face = screen, color = (0,200,200)):                 # draw wireframe
    lines = obj.line
    verts = obj.verts
    verts2d = obj.verts2d
    for i in lines:
        start = verts2d[i[0]]
        end = verts2d[i[1]]
        pygame.draw.line(face, color, start, end)

def wireframe_grad(obj, face = screen, grad = rainbow):              	# draw gradient wire Frame.
    lines = obj.line
    verts = obj.verts
    verts2d = obj.verts2d
    for i in lines:
        start = verts2d[i[0]]
        end = verts2d[i[1]]
        color = grad.getColor(vector.angle(verts[i[0]], (0,-1,0))/(2*pi))
        pygame.draw.line(face, color, start, end)
  


def wireframe_line(obj, face = screen, color = (200,200,200)):
    lines = obj.line
    for i in lines:
        vect1 = verts[i][0]
        vect2 = verts[i][1]
        start 	= projection.projtype(vect1)
        end 	= projection.projtype(vect2)
        pygame.draw.line(face, color, start, end)
        
    pass


def sort_polys(obj):
    polys = obj.poly
    verts = obj.verts
    #polys = [(0,1,2),(0,1,3), (0,1,4), (2,3,4)]
    #verts = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(1,1,1),(1,0,1)]
    cp = cam.pos
    
    # does not work in python3 
    # middpoint = lambda (x0,y0,z0),(x1,y1,z1),(x2,y2,z2): ((x0+x1+x2)/3.0, (y0+y1+y2)/3.0, (z0+z1+z2)/3.0)
    # distance_pow_2 = lambda (x0,y0,z0),(x1,y1,z1): (x1-x0)*(x1-x0) + (y1-y0)*(y1-y0) + (z1-z0)*(z1-z0)
    
    def middpoint(pos0, pos1, pos2):
        return ((pos0[0]+pos1[0]+pos2[0])/3, (pos0[1]+pos1[1]+pos2[1])/3, (pos0[2]+pos1[2]+pos2[2])/3)
    
    def distance_pow_2(pos0, pos1):
        return (pos1[0]-pos0[0])**2 + (pos1[1]-pos0[1])**2 + (pos1[2]-pos0[2])**2
    
    poly_sorted = sorted(polys, key = lambda x: -1*distance_pow_2(cp, middpoint(verts[x[0]],verts[x[1]],verts[x[2]])))
    return poly_sorted

rendertype = shade
point_index = False

# -----------------------------Testing code ----------------------------
if __name__ == "__main__":
    print(blackwhite)
    rainbow.show()
    fire.show(0,50)
    water.show(0,100)
    blackwhite.show(0,150)
    turquoise.show(0,200)
    bluepurp.show(0,250)
    stripped.show(0,300)
    clay.show(0,350)
    pygame.display.flip()
        
        
    while True:
        pygame.event.get()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    
        


