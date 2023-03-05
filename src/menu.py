import pygame
import sys
import projection
import transform
import geo
import shader
import mouse
import gui
import cam

def make_sphere():
    my_object = geo.sphere(14, 12, radius = 5)                         # create sphere
    
options = gui.dropdown("Options",  820, 20, ["Create","Camera","Lathe","Render Options","Settings"])
index = 0
proj_options = gui.dropdown("Projection",  840, 70, ["Ortonormal","Perspective", "Perspective easy"])
proj_index = 1

grad_options = gui.dropdown("Gradient",  840, 120, ["Rainbow","Fire","water","BlackWhite","Turquoise","Blue Purple", "Red Clay"])
grad_index = 1

render_options = gui.dropdown("Render Type", 840, 170, ["Shade", "WireFrame", "Points"]) 
render_index = 1

point_index_toggle = gui.toggle("Point Index", 860, 220, shader.point_index)

class setting_values:
    def __init__(self, values, sliders):
        self.values = values
        self.sliders = sliders
        for i in range(0,len(sliders)):
            self.sliders[i].set_value(values)
    
    
#torus_s1 = setting_values([24, 3], [gui.slider("seg1:", 840, 120, 6,28), gui.slider("Outer radius:", 840, 170, 1.5, 4)])
torus_s1 = 28
torus_s2 = 18
torus_r1 = 3
torus_r2 = 1.4

shape_opt = [geo.sphere(18, 15, radius = 5),geo.cube(4,8,2),geo.cylinder(40,8,5),geo.torus(torus_s1,18,3,1.4), geo.lathe(30)]
shape_options = gui.dropdown("Select Shape", 840, 70, ["Sphere", "Box", "Cylinder", "Torus", "lathe"])


def create():
    shape_options.run()
    if shape_options.change:
        geo.TheObject = shape_opt[shape_options.get_value()-1]
        pass
        

def camera():
    pass
    
def lathe():
    pass
    
def render():
    global proj_index
    proj_opt = [projection.orto, projection.persp, projection.persp_easy]
    grad_opt = [shader.rainbow, shader.fire, shader.water, shader.blackwhite, shader.turquoise, shader.bluepurp, shader.clay]
    render_opt = [shader.shade, shader.wireframe_grad, shader.draw_points]
    
    if shader.rendertype == shader.draw_points:
        point_index_toggle.run()
        shader.point_index = point_index_toggle.get_value()
    
    render_options.run()
    if render_options.change:
        shader.rendertype = render_opt[render_options.get_value()-1]
        
    grad_options.run()
    if grad_options.change:
        shader.maingrad = grad_opt[grad_options.get_value()-1]
        print("the chader is: \n",shader.maingrad)
        
    proj_options.run()
    if proj_options.change:
        proj_index = proj_options.get_value()-1
        projection.projtype = proj_opt[proj_index]
    
def settings():
    pass

functions = [create, camera, lathe, render, settings]



def run():
    global options, index
    options.run()                                                  # menu options
    if options.change:
        index = options.get_value()-1
    if not options.active:
        functions[index]()
    pass



if __name__ == "__main__":
    pass
