
#SP1 et 1bis) Fixer l'orientation pour faire allere vers la coordonée X ou Y de VOLDEMORT

def reorientation_north() :
    while get_direction!=NORTH :
        if get_direction==WEST
            turn_right()
        elif get_direction==EAST
            turn_left()
        else 
            turn_right()
def reorientation_south() :
    while get_direction!=SOUTH :
        if get_direction==WEST
            turn_left()
        elif get_direction==EAST
            turn_right()
        else 
            turn_right()
            turn_right()
            
def reorientation_east():
    while get_direction!=EAST:
        if get_direction==WEST:
            turn_right()
            turn_right()
        elif get_direction != NORTH:
            turn_right()
        else:
            turn_left()
def reorientation_west() :
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

while get_target_x != get_x
    #while is_in_front_of_enemy
    while can_move:
    #Il faut mettre NORD ou SUD
        if get_target_x>get_x():
            reorientation_east()
            move()
        elif get_target_x < get_x:
            reorientation_west()
            move()
        #SP3 bis
    while can_move==false 
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
while get_target_y != get_y

    while can_move:
    #Il faut mettre NORD ou SUD
        if get_target_y>get_y():
           turn_right()
        elif get_target_x > get_x:
            turn_right()
           reorientation_south()
            move()
        elif get_target_y < get_y:
            reorientation_north()
            move()
    while can_move==false:
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