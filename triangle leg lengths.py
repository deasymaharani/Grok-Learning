import math as m

def triangle_legs(hyp, angle):
    if hyp > 0 and 0<=angle<=90:
        leg_a = m.cos(m.radians(angle)) * hyp
        leg_o = m.sin(m.radians(angle)) * hyp
        if leg_o < leg_a:
            legs = (leg_o, leg_a)
        else:
            legs = (leg_a, leg_o)
        return legs
    else:
        return False
        
        
