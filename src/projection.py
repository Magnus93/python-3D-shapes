import pygame
import vector
import transform
import cam
from math import *

view_midd = (395,395)
camview = 2.0
orto_scale = 70

def set_view_size(x,y):
	global view_midd
	view_midd = (x/2, y/2)
	

def orto(point):									# ortogonal projection
    global orto_scale
    x = -int(point[0]*orto_scale) + view_midd[0]
    y = -int(point[1]*orto_scale) + view_midd[1]
    return (x,y)

def persp(point):
    global view_midd, camview, cam_pos
    u3 = vector.sub(cam.pos, point)
    vxc = vector.dot_prod(u3, cam.side)        # x cooardinate in cameras base
    vyc = vector.dot_prod(u3, cam.up)		   # y cooardinate in cameras base
    vzc = vector.dot_prod(u3, cam.direct)	   # z cooardinate in cameras base
    vc = vector.normalize((vxc, vyc, vzc))
    vxc = vc[0]
    vyc = vc[1]
    px = view_midd[0] + (vxc)*view_midd[0]*camview
    py = view_midd[1] + (vyc)*view_midd[1]*camview
    return (int(px),int(py))

def persp_easy(point):
    global view_midd, camview, cam_pos
    u3 = vector.sub(cam.pos, point)
    vxc = vector.dot_prod(u3, cam.side)								# x cooardinate in cameras base
    vyc = vector.dot_prod(u3, cam.up)								# y cooardinate in cameras base
    vzc = vector.dot_prod(u3, cam.direct)								# z cooardinate in cameras base
    px = view_midd[0] - (vxc/vzc)*view_midd[0]*camview
    py = view_midd[1] - (vyc/vzc)*view_midd[1]*camview
    return (int(px),int(py))

def persp_angle(point, cam_angle = pi/6):
    global view_midd
    u3 = vector.sub(cam.pos, point)
    vxc = vector.dot_prod(u3, cam.side)								# x cooardinate in cameras base
    vyc = vector.dot_prod(u3, cam.up)								# y cooardinate in cameras base
    vzc = vector.dot_prod(u3, cam.direct)							# z cooardinate in cameras base
    alfax = atan(vxc/vzc)
    alfay = atan(vyc/vzc)
    if vxc < 0:
        alfax = alfax
    if vyc < 0:
        alfay = alfay
    px = view_midd[0] - (alfax*3*camview/pi)*view_midd[0]
    py = view_midd[1] - (alfay*3*camview/pi)*view_midd[1]
    return (int(px),int(py))

projtype = orto

# -----------------------------Testing code ----------------------------

if __name__ == "__main__":
    def main():
        persp((5,0,0))
        print("\n")
        print(persp_angle((-5,0,0)))
        print("\n")
        print(persp((-5,0.00001,0)))
    
    
    main()
