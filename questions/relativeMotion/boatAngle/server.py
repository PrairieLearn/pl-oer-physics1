import random, math
def generate(data):
    boat=random.choice([4,5,6]); current=random.choice([1,2]); angle=math.degrees(math.asin(current/boat))
    # Distractors represent using the complementary angle, subtracting the
    # current from the boat speed, or adding an arbitrary angle.
    data['params'].update(boat=boat,current=current,correct=f'{angle:.1f}',a=f'{90-angle:.1f}',b=f'{math.degrees(math.atan(current/boat)):.1f}',c=f'{angle+15:.1f}')
