import random, math
def generate(data):
    car=random.choice([35,42,49]); ball=random.choice([18,21,24]); angle=random.choice([30,40,50])
    x=ball*math.cos(math.radians(angle)); y=ball*math.sin(math.radians(angle)); r=math.hypot(x, y+car)
    data['params'].update(car=car,ball=ball,angle=angle,correct=f'{r:.1f}',a=f'{math.hypot(x,y):.1f}',b=f'{math.hypot(x,car-y):.1f}',c=f'{car+ball:.1f}')
