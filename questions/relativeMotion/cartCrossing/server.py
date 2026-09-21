import random, math
def generate(data):
    cart=random.choice([3,4,5]); walker=random.choice([1,2]); width=random.choice([18,24,30]); t=width/walker; ground=math.hypot(cart+walker,0); drift=cart*t
    answers=[round(drift,1),round(width/(walker+1),1),round(cart+walker+2,1),round(math.hypot(cart,walker),1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.1,1)
    data['params'].update(cart=cart,walker=walker,width=width,time=f'{t:.1f}',correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}')
