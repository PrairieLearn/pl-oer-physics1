import random
def generate(data):
    width=random.choice([45,55,65]); speed=random.choice([3,4,5]);
    data['params'].update(width=width,speed=speed,correct=f'{width/speed:.1f}',a=f'{width/(speed+1):.1f}',b=f'{width/(speed-1):.1f}',c=f'{width*speed:.1f}')
