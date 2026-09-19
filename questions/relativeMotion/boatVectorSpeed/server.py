import random, math
def generate(data):
    north=random.choice([3,4,5]); east=random.choice([2,3,4]); r=math.hypot(north,east)
    data['params'].update(north=north,east=east,correct=f'{r:.1f}',a=f'{north+east:.1f}',b=f'{abs(north-east):.1f}',c=f'{r+1:.1f}')
