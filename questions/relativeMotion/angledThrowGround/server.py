import random, math
def generate(data):
    car=random.choice([12,16,20]); throw=random.choice([10,12,14]); ang=random.choice([30,45,60]); x=throw*math.cos(math.radians(ang)); y=throw*math.sin(math.radians(ang)); ground=math.hypot(car+x,y); direction=math.degrees(math.atan2(y,car+x))
    data['params'].update(car=car,throw=throw,ang=ang,correct=f'{ground:.1f}',direction=f'{direction:.1f}',a=f'{car+throw:.1f}',b=f'{math.hypot(car-x,y):.1f}',c=f'{throw:.1f}')
