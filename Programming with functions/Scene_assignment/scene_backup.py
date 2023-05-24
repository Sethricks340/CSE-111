"""
This also has the grid in it for future reference
-Seth
""" 
 

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    

    draw_background(canvas, scene_width, scene_height)

    draw_sun(canvas, 700, 400, 50)

    draw_cloud(canvas, 300, 300)
    draw_cloud(canvas, 100, 350)
    draw_cloud(canvas, 400, 400)

    for i in range (50, 800, 200): 
        draw_pine_tree(canvas, i, 200, 80)

    for i in range (150, 850, 200):
        draw_coniferous_tree(canvas, i, 200, 80)


    for i in range(1, 180, 10):

        for x in range(1, 134):
            draw_grass(canvas, 6 * x, 175 - i, 30)

    draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_pine_tree(canvas, center_x, bottom, height):

    #draw the trunk of the tree.
    trunk_width = height / 10
    trunk_hieght = height / 8
    left_trunk = center_x - trunk_width / 2 
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2 
    trunk_top = bottom + trunk_hieght
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill = "tan4")
    
    #Draw the skirt of the tree
    skirt_width = height / 2 
    skirt_left =  center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height 
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill= "forestGreen")

def draw_coniferous_tree(canvas, center_x, bottom, height):
    
    #draw the trunk of the tree
    trunk_width = height / 10
    trunk_hieght = height / 4
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_hieght
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill = "tan4")

    #Draw the circle of the tree
    bottom_left_x = center_x - 0.5 * height 
    bottom_left_y = bottom + .75 * trunk_hieght
    top_right_x = center_x + 0.5 * height
    top_right_y = bottom + height
    draw_oval(canvas, bottom_left_x, bottom_left_y, top_right_x, top_right_y, fill= "forestGreen")


def draw_grid(canvas, width, height, interval):
    #Draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    #Draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


def draw_background(canvas, scene_width, scene_height):

    #draw ground
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill= "saddleBrown")

    #draw sky
    draw_rectangle(canvas, 0, 200, scene_width, scene_height, fill= "deepSkyBlue")


def draw_sun(canvas, center_x, center_y, radius):

    #draw sun center
    bottom_left_x = center_x - radius
    bottom_left_y = center_y - radius
    top_right_x = center_x + radius
    top_right_y = center_y + radius
    draw_oval(canvas, bottom_left_x, bottom_left_y, top_right_x, top_right_y, outline= "yellow", fill= "yellow1")

    #draw sun rays
    for i in range(0, 3):
        
        #center lines:
        if i < 2:
            draw_line(canvas, center_x, center_y - radius + 2 * i * radius, center_x, center_y - 2 * radius + 4 * i * radius, width= 5, fill= "yellow1")

        #left lines:
        draw_line(canvas, center_x - 2 * radius, center_y - 2 * radius + 2 * i * radius, center_x - radius, center_y - 1 * radius + i * radius, width= 5, fill= "yellow1")

        #right lines:
        draw_line(canvas, center_x + 2 * radius, center_y - 2 * radius + 2 * i * radius, center_x + radius, center_y - 1 * radius + i * radius, width= 5, fill= "yellow1")


def draw_cloud(canvas, bottom_left_x, bottom_left_y):


    #draw left oval
    draw_oval(canvas, bottom_left_x, bottom_left_y, bottom_left_x + 100, bottom_left_y + 50, outline= "white", fill= "white")

    #draw right oval
    draw_oval(canvas, bottom_left_x + 50, bottom_left_y, bottom_left_x + 150, bottom_left_y + 50, outline= "white", fill= "white")

    #draw middle oval
    draw_oval(canvas, bottom_left_x + 25, bottom_left_y + 25, bottom_left_x + 125, bottom_left_y + 75, outline= "white", fill= "white")

def draw_grass(canvas, center_x, bottom, height):

    bottom_x = center_x - 2
    bottom_y = bottom
    top_x = center_x + 2
    top_y = bottom + height

    draw_rectangle(canvas, bottom_x, bottom_y, top_x, top_y, fill= "springGreen3")

#    draw_oval(canvas, bottom_left_x)
# Call the main function so that
# this program will start executing.
main()