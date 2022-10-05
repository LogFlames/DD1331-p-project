# Class lighted sphere
#    instvars: radius, light x, light y
#    method to validate new light x and light y
#    static method to create instance of lighted sphere from user input and makes sure the input is valid

# Render Function: takes parameter [sphere (lighted sphere), resolution, render_window_size], returns a 2d-array (resolution x resolution in size) with floats normalized between 0 and 1 indicating the brightness at that pixel, if the point is outside the sphere it shall be -1, assuming there in a sphere at the center with a radius of sphere.radius and a light at (sphere.lightx,sphere.lighty). The render_window_size decides how large of an area to render. (from coords (-rws,-rws) to coords (rws,rws)) If the sphere radius and render_window_size are the same, the sphere will just touch the edges of the brightness_map. If the render_window_size is larger than the spheres radius there will be a border

# Terminal visualize function:
#     Parameters: brightness-map from the render function
# File visualize function: 
#     Parameters: brightness-map from the render function

# TkInter Class
#   Init tkinter, create window
#   On creation and when sphere-inst-vars are updated: render sphere using the render-function and display it to the screen using the user-supplied color-resolution
#   Let user enter sphere radius, render resolution and color-resolution
#   On click event:
#       get new x,y position of light and check if they are on the surface of the sphere - if they are, update the sphere

# main function
#    Ask which mode of rendering the user wants
#
#    if terminal or file:
#        Ask the user for values for radius and light x and light y
#        Create the sphere object
#        Render it and pass the brightness-map to the terminal/file visualize function
#    if tkinter:
#        Create a default sphere with x,z at 0,0 and appropriate radius
#        Open the window and let the user click away

