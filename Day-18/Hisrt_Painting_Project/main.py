from turtle_drawing import HirstDrawing
from random import choice

# import colorgram
#
# colors = colorgram.extract('Image.jpg',50)
# color_list = []
# for obj in colors:
#     r_value = obj.rgb.r
#     g_value = obj.rgb.g
#     b_value = obj.rgb.b
#     color_list.append((r_value, g_value, b_value))
# print(color_list)

color_list = [(243, 243, 245), (244, 241, 233), (48, 95, 140), (215, 154, 104), (163, 80, 44), (234, 242, 238),
              (242, 234, 239), (224, 209, 106), (16, 36, 59), (186, 163, 24), (55, 29, 18), (118, 164, 204),
              (126, 68, 94), (163, 19, 9), (210, 91, 68), (42, 129, 68), (194, 139, 160), (124, 182, 157), (57, 28, 40),
              (128, 27, 43), (19, 52, 43), (195, 90, 113), (46, 170, 98), (38, 62, 97), (27, 90, 53), (236, 162, 188),
              (226, 206, 1), (108, 118, 172), (4, 89, 109), (64, 82, 30), (227, 177, 168), (137, 215, 197),
              (168, 183, 218), (49, 146, 196), (167, 201, 211)]

k = HirstDrawing()
k.kasav_screen_setup()
k.kasav_properties(sp=15,wd=10)

k.set_position(-255, -255)

for row_dot in range(10):
    if row_dot % 2 == 0:
        start_angle = 0
    else:
        start_angle = 180
    k.set_direction(90)
    k.pen_up()
    k.dot_forward(50)
    k.pen_down()
    k.set_direction(start_angle)
    for column_dot in range(10):
        k.draw(rgb_value=choice(color_list))
        k.pen_up()
        k.dot_forward(50)
        k.pen_down()




k.kasav_screen_exit()
