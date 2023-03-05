import pygame
from math import *


screen = pygame.display.set_mode((800,600))#,pygame.FULLSCREEN)
mytimer = pygame.time.Clock()

def rot_x(point,beta):
    x = point[0]
    y = point[1]
    z = point[2]
    return [x,(y*cos(beta)-z*sin(beta)),(y*sin(beta)+z*cos(beta))]
    
def rot_y(point,beta):
    x = point[0]
    y = point[1]
    z = point[2]
    return [(x*cos(beta)+z*sin(beta)),y,(-x*sin(beta)+z*cos(beta))]

def rot_z(point,alfa):
    x = point[0]
    y = point[1]
    z = point[2]
    return [(x*cos(alfa)-y*sin(alfa)),(x*sin(alfa)+y*cos(alfa)),(z)]


def scale(point, scale):
    return (point[0]*scale, point[1]*scale, point[2]*scale)
    
    
def move(point, offset):         #translate
    point = (point[0]+offset[0], point[1]+offset[1], point[2]+offset[2])
    return point




if __name__ == "__main__":
    
    def main():
        pass
        
        
    main()

