import random, math
def generate(data):
    car=random.choice([14,18,22]); north=random.choice([6,8,10]);
    r=math.hypot(car,north)
    data['params'].update(car=car,north=north,correct=f'{r:.1f}',a=f'{car+north:.1f}',b=f'{abs(car-north):.1f}',c=f'{r+2:.1f}')
