import random, math
def generate(data):
    air=random.choice([20,25,30]); wind=random.choice([8,10,12]); north=random.choice([3,4]); ground=math.hypot(math.sqrt(air**2-wind**2),north); angle=math.degrees(math.asin(wind/air));
    data['params'].update(air=air,wind=wind,north=north,correct=f'{angle:.1f}',a=f'{math.degrees(math.atan(wind/air)):.1f}',b=f'{90-angle:.1f}',c=f'{angle+15:.1f}')
