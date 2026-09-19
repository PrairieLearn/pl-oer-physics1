import random, math
def generate(data):
    air=random.choice([20,25,30]); wind=random.choice([4,6,8]);
    angle=math.degrees(math.asin(wind/air))
    data['params'].update(air=air,wind=wind,correct=f'{angle:.1f}',a=f'{90-angle:.1f}',b=f'{angle+10:.1f}',c=f'{angle+20:.1f}')
