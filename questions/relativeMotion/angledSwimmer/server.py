import random, math
def generate(data):
    swim=random.choice([2.5,3,3.5]); current=random.choice([1,1.5]); angle=random.choice([30,45,60]); x=swim*math.cos(math.radians(angle))+current; y=swim*math.sin(math.radians(angle)); r=math.hypot(x,y)
    data['params'].update(swim=f'{swim:g}',current=f'{current:g}',angle=angle,correct=f'{r:.1f}',a=f'{swim+current:.1f}',b=f'{math.hypot(swim*math.cos(math.radians(angle)),swim*math.sin(math.radians(angle))):.1f}',c=f'{abs(swim-current):.1f}')
