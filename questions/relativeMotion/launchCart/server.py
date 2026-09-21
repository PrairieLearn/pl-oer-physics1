import random, math
def generate(data):
    cart=random.choice([6,8,10]); launch=random.choice([5,6,7]); ang=random.choice([30,45,60]); x=cart+launch*math.cos(math.radians(ang)); y=launch*math.sin(math.radians(ang)); direction=math.degrees(math.atan2(y,x))
    answers=[round(direction,1),round(ang,1),round(90-direction,1),round(math.degrees(math.atan2(launch,cart)),1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.1,1)
    data['params'].update(cart=cart,launch=launch,ang=ang,correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}')
