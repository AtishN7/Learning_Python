from turtle_moves import MoveTurtle

kas = MoveTurtle()

kas.kasav_screen_setup()
kas.kasav_shape(3)
# kas.square_move(paces=100, angle=90)
# kas.dotted_line(line_paces=10)
kas.draw_pattern(shape_sides=11, shape_length=100)
kas.kasav_screen_exit()

