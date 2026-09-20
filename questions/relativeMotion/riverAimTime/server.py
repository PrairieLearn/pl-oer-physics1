import random, math
def generate(data):
    w=random.choice([60,80,100]); cur=random.choice([3,4]); boat=random.choice([5,6,7]); north=math.sqrt(boat**2-cur**2); angle=math.degrees(math.asin(cur/boat)); t=w/north
    data['params'].update(w=w,cur=cur,boat=boat,angle=f'{angle:.1f}',time=f'{t:.1f}',a=f'{90-angle:.1f}',b=f'{w/boat:.1f}',c=f'{w/north+5:.1f}')
