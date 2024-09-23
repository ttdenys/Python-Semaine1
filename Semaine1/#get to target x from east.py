#get to target x from east
def set_orientation_west() :
    while get_direction != WEST:
        if get_direction==EAST:
            turn_right()
            turn_right()
        elif get_direction != NORTH:
            turn_left()
        else:
            turn_right()
if get_direction!=west:
    set_orientation_west()
while get_x!=get_target_x:
    while can_move== True and not is_in_front_of_enemy:
        move 
        set_orientation_west
        if not is_in_front_of_enemy AND if can move== True:
            move
            #on a resolu le sp1
    while not can_move:
        turn_right
        if not is_in_front_of_enemy AND if can move== True:
            move 
        while not can_move:
            turn_right
        if can_move: 
            move
        turn_left
        #sp2 fini
    while is_in_front_of_enemy:
        turn_right
        if not is_in_front_of_enemy AND if can move== True:
            move 
        else:
            turn_right
        turn_left
#SP3 FIN
if get_direction!=west:
    set_orientation_west()