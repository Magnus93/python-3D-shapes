import mouse
import transform
from math import *
pos = (0,0,14)
pos0 = pos
up = (0,1,0)
side = (1,0,0)
direct = (0,0,-1)

pan_active = False
pan_start = (0,0)

def dictance(point):
	return sqrt((pos[0]-point[0])**2+(pos[1]-point[1])**2+(pos[2]-point[2])**2)

def rot(pos_start, pos_stop):
	(x,y) = pos_start
	(x_stop, y_stop) = pos_stop 
	global pos, pos0, up, direct, side
	dr_c = 120
	if x_stop != 0 or y_stop != 0:
		pos0 = pos
	pos = transform.rot_y(pos0,(x+0.0)/dr_c)
	direct = transform.rot_y(direct,(x+0.0)/dr_c)
	up = transform.rot_y(up,(x+0.0)/dr_c)
	#pos = transform.rot_y(transform.rot_x(pos0,(y+0.0)/dr_c),(-x+0.0)/dr_c)
	pass

def pan():
	global pos, pos0, pan_active
	if mouse.down[1]:
		pan_active = True
		pan_start = mouse.pos
	if mouse.up[1]:
		pan_active = False
	if pan_active:
		dif = (mouse.pos[0]-pan_start[0], 0)
		pos = (pos[0]+dif[0]*0.5, pos[1])
		
		
		
	#pos0 = (pos[0]+x*0.01, pos[1]+y*0.01)
	#pos = pos0
	
'''
dr_c = 120
if x_stop != 0 or y_stop != 0:
	self.verts0 = self.verts
ls_po = []
for i in self.verts0:
	ls_po.append(transform.rot_y(transform.rot_x(i,(y+0.0)/dr_c),(-x+0.0)/dr_c))
self.verts = ls_po
'''
