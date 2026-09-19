import random, math
def generate(data):
    floatv=random.choice([4,5,6]); walker=random.choice([2,3]); angle=random.choice([30,45,60]); x=walker*math.cos(math.radians(angle)); y=walker*math.sin(math.radians(angle)); r=math.hypot(floatv+x,y)
    data['params'].update(floatv=floatv,walker=walker,angle=angle,correct=f'{r:.1f}',a=f'{floatv+walker:.1f}',b=f'{math.hypot(floatv,y):.1f}',c=f'{math.hypot(x,y):.1f}')
