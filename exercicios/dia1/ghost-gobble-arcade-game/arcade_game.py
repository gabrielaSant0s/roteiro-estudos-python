def eat_ghost(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if ( power_pellet_active == True ) and ( touching_ghost == True ):
        return True
    else:
        return False 


def score(touching_power_pellet, touching_dot):
    """
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    if ( touching_power_pellet == True ) or ( touching_dot == True ):
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    if ( touching_ghost == True ) and ( power_pellet_active == False ):
        return True
    else:
        return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if ( has_eaten_all_dots == True ):
        if ( power_pellet_active == True ):
            return True
        elif ( power_pellet_active == False ) and ( touching_ghost == True):
            return False
        else:
            return True
    else:
        return False 
        

