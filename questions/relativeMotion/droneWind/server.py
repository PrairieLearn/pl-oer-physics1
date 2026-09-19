import random, math
def generate(data):
    drone=random.choice([12,15,18]); wind=random.choice([5,6,7]); r=math.sqrt(drone**2-wind**2)
    data['params'].update(drone=drone,wind=wind,correct=f'{r:.1f}',a=f'{drone+wind:.1f}',b=f'{drone-wind:.1f}',c=f'{math.sqrt(drone**2+wind**2):.1f}')
