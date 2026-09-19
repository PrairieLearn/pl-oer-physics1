import random, math
def generate(data):
    air=random.choice([20,25,30]); wind=random.choice([5,6,8]);
    speed=math.sqrt((air*math.cos(math.radians(30))-wind)**2+(air*.5)**2)
    data['params'].update(air=air,wind=wind,correct=f'{speed:.1f}',a=f'{air+wind:.1f}',b=f'{abs(air-wind):.1f}',c=f'{math.sqrt(air**2+wind**2):.1f}')
