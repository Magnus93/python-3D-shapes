import pygame
import sys
import mouse
import gui
from math import *
import transform
import projection
import geo
import shader 
import menu
import cam
mytimer = pygame.time.Clock()

screen = pygame.display.set_mode((1200 , 800))
pygame.display.set_caption ("3D_version_4")
view = pygame.Surface((790,790))
menuface = pygame.Surface((390,790))
exitbutton = gui.exit_butt(1145)                                        # create exit button

def main():
    global view, menu

    def apply_scale():
        scale = scale_slider.get_value()
        mysphere.scale(scale)
    projection.projtype = projection.persp                          # set projection type

    while True:
        mouse.run()                                                     # get mouse input
        screen.fill((15,15,15))
        view.fill((50,50,60))
        menuface.fill((40,40,50))
        shader.rendertype(geo.TheObject, view, shader.maingrad)
        #shader.wireframe_color(my_object, view)                         # draw wireframe
        #shader.wireframe_line(my_object, view)
        geo.origin_show(view)
        if 5 < mouse.pos[0] < 795:                                      # only drag if mouse within view Surface
                        geo.TheObject.rot(mouse.drag_curr,mouse.drag_stop)              # ----------------||--------------------
                        #cam.rot(mouse.drag_curr, mouse.drag_stop)
                        geo.TheObject.proj2d()
        screen.blit(view, (5,5))                                        # blit view
        screen.blit(menuface, (803,5))                                      # blit menu
        menu.run()                                                      # run menu
        exitbutton.run()
        if mouse.down[3]:
            cam.pos = (0,0,cam.pos[2]/1.1)
            projection.orto_scale *=  1.1
        if mouse.down[4]:
            cam.pos = (0,0,cam.pos[2]*1.1)
            projection.orto_scale /=  1.1
        cam.pan()
        pygame.display.flip()                                           # update display
        mytimer.tick(24)                                                # keep 60 frames/sec


if __name__ == "__main__":
    main()
