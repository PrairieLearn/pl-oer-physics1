import random, math
def generate(data):
    platform=random.choice([3,4,5]); launch=random.choice([2,3,4]); ang=random.choice([30,45,60]); x=platform+launch*math.cos(math.radians(ang)); y=launch*math.sin(math.radians(ang)); speed=math.hypot(x,y)
    data['params'].update(platform=platform,launch=launch,ang=ang,correct=f'{speed:.1f}',a=f'{platform+launch:.1f}',b=f'{math.hypot(platform,launch):.1f}',c=f'{launch:.1f}')
