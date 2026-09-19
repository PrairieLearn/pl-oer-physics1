import random, math
def generate(data):
    across=random.choice([60,70,80]); t=random.choice([30,35,40]); boat=random.choice([5,6,7])
    current=math.sqrt(boat**2-(across/t)**2)
    data['params'].update(across=across,t=t,boat=boat,correct=f'{current:.2f}',a=f'{current+1.0:.2f}',b=f'{abs(boat-across/t):.2f}',c=f'{boat+across/t:.2f}')
