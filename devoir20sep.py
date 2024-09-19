
#SP1 et 1bis) Fixer l'orientation pour faire allere vers la coordonée X ou Y de VOLDEMORT

def set_orientation_north():
    while get_direction!=NORTH :
        if get_direction==WEST:
            turn_right()
        elif get_direction==EAST:
            turn_left()
        else :
            turn_right()
def set_orientation_north_easy ():
    while get_direction!=NORTH :
        turn_right
    
def set_orientation_south():
    while get_direction!=SOUTH :
        if get_direction==WEST:
            turn_left()
        elif get_direction==EAST:
            turn_right()
        else :
            turn_right()
            turn_right()
            
def set_orientation_east():
    while get_direction!=EAST:
        if get_direction==WEST:
            turn_right()
            turn_right()
        elif get_direction != NORTH:
            turn_right()
        else:
            turn_left()
def set_orientation_west() :
    while get_direction != WEST:
        if get_direction==EAST:
            turn_right()
            turn_right()
        elif get_direction != NORTH:
            turn_left()
        else:
            turn_right()
#######
#SP2 bis

while get_target_x != get_x :
    #while is_in_front_of_enemy
    while can_move==true or not is_in_front_of_enemy :
    #Il faut mettre NORD ou SUD
        if get_target_x>get_x():
            set_orientation_east()
            move()
        elif get_target_x < get_x:
            set_orientation_west()
            move()
        #SP3 bis
    while not can_move or is_in_front_of_enemy==true : 
        if get_target_x < get_x:
            turn_left()
            move()
            turn_right ()
        elif get_target_x > get_x:
            turn_right()
            move()
            turn_left()
       
print ("Harry is facing Voldemort")
########

#SP2 vers une des coordonees de voldemort (Y ou X)
#On fait les Y
#SP3 countornement des obstacles pour les Y
while get_target_y != get_y :

    while can_move:
    #Il faut mettre NORD ou SUD
        if get_target_y>get_y():
           turn_right()
        elif get_target_x > get_x:
            turn_right()
            set_orientation_south()
            move()
        elif get_target_y < get_y:
            set_orientation_north()
            move()
    while not can_move:
        if get_target_y < get_y:
            turn_left()
            move()
            turn_right()
        elif get_target_y > get_y:
            turn_right()
            move()
            turn_left()

if get_target_y==get_y :
    print ("Strike !")