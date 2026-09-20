import random, math
def generate(data):
    w=random.choice([48,60,72]); boat=random.choice([5,6,7]); cur=random.choice([2,3]); t=w/boat; drift=cur*t
    data['params'].update(w=w,boat=boat,cur=cur,correct=f'{drift:.1f}',a=f'{cur*w/(boat+cur):.1f}',b=f'{w/cur:.1f}',c=f'{math.hypot(w,drift):.1f}')
