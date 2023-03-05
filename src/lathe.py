import pygame
import sys
import mouse
import gui
from math import *
import transform
import projection
import geo
import shader 
mytimer = pygame.time.Clock()
pygame.font.init()
smallfont = pygame.font.SysFont("verdana", 14)

def null():
    print "Nothing"

screen = pygame.display.set_mode((1200 , 800))
view = pygame.Surface((790,790))
menu = pygame.Surface((390,790))                                        
exitbutton = gui.exit_butt(1145)                                        # create exit button
modetoggle = gui.toggle("Set Points Mode", 820,30,True)
lathe_points = [(1,-1),(1,1)]
my_object = geo.sphere(24, 18, radius = 5)                         # create sphere

def set_points_mode():
    global view, lathe_points
    x,y = mouse.pos
    w = view.get_width()
    pygame.draw.line(view, (150,150,180), (w/2,20), (w/2,780))          # midd line
    for i in range(len(lathe_points)):
        p1 = (w/2+100*lathe_points[i][0], w/2+100*lathe_points[i][1])
        if p1[0] < x < p1[0]+10 and p1[1] < y < p1[1]+10:
            render_move = smallfont.render("Move",1, (230,230,255))     # upper value
            view.blit(render_move, (x+5,y-10))
            if mouse.down[0]:
                print "press", i
                mouse.drag_curr
        pygame.draw.line(view, (0,200,250), (p1[0]-2,p1[1]-2),(p1[0]+2,p1[1]+2))
        pygame.draw.line(view, (0,200,250), (p1[0]-2,p1[1]+2),(p1[0]+2,p1[1]-2))
        if i < len(lathe_points)-1:
            p2 = (w/2+100*lathe_points[i+1][0], w/2+100*lathe_points[i+1][1])
            pygame.draw.line(view, (200,200,250), p1, p2)
        
    
def view_mode():
    global my_object
    shader.shade(my_object, view, shader.rainbow)                       # draw wireframe
    shader.wireframe_grad(my_object, view)                              # draw wireframe
    if 5 < mouse.pos[0] < 795:                                          # only drag if mouse within view Surface
        my_object.rot(mouse.drag_curr,mouse.drag_stop)                  # ----------------||--------------------
    if mouse.down[3]:
        projection.cam_pos = (0,0,projection.cam_pos[2]/1.1)
    if mouse.down[4]:
        projection.cam_pos = (0,0,projection.cam_pos[2]*1.1)    


def main():
    global view, menu
    #my_object = geo.cube(4,8,2)                                        # create cube
    #my_object = geo.cylinder(40, 8, 5)                                        # create cylinder
    
    def apply_scale():
        scale = scale_slider.get_value()
        mysphere.scale(scale)
    shader.projtype = projection.persp									# set projection type
    
    while True:
        mouse.run()                                                     # get mouse input
        screen.fill((15,15,15))                                         
        view.fill((50,50,60))
        menu.fill((40,40,50))
        #shader.draw_points(my_object, view, index = True)                              # draw verts
        screen.blit(menu, (803,5))                                      # blit menu
        modetoggle.run()
        if modetoggle.get_value():
            set_points_mode()
        else:
            view_mode()
        screen.blit(view, (5,5))                                        # blit view                
        exitbutton.run()
        pygame.display.flip()                                           # update display
        mytimer.tick(60)                                                # keep 60 frames/sec
		

if __name__ == "__main__":
	main()
