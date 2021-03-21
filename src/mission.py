def recalculate_motor_data(current_state, windinfo, direction_final_destination):
    coordX = current_state[0]
    coordY = current_state[1]

    ensight.variables.evaluate("U = (2*3.1415927*1350/60)*SQRT(cordX^2+cordY^2)")
    ensight.variables.evaluate("W_X = velocity[X] - U_X")
    ensight.variables.evaluate("W_Y = velocity[Y] - U_Y")

