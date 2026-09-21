import random, math
def generate(data):
    floatv=random.choice([4,5,6]); walker=random.choice([2,3]); ang=random.choice([30,45,60]); x=walker*math.cos(math.radians(ang)); y=walker*math.sin(math.radians(ang)); speed=math.hypot(floatv+x,y)
    data['params'].update(floatv=floatv,walker=walker,ang=ang,correct=f'{speed:.1f}',a=f'{floatv+walker:.1f}',b=f'{math.hypot(floatv,y):.1f}',c=f'{walker:.1f}')
