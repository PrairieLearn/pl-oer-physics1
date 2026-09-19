import random
def generate(data):
    t1=random.choice([1.5,1.8,2.0]); run=random.choice([2.0,2.5,3.0]); t2=random.choice([3.0,3.5,4.0])
    # d/v relations: d=v_band*t1 and d=(v_band-run)*t2.
    vb=run*t2/(t2-t1); d=vb*t1
    answers=[round(d,2), round(vb*t2,2), round(run*t1,2), round(d+run,2)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.01,2)
    data['params'].update(t1=f'{t1:g}',run=f'{run:g}',t2=f'{t2:g}',distance=f'{answers[0]:.2f}',a=f'{answers[1]:.2f}',b=f'{answers[2]:.2f}',c=f'{answers[3]:.2f}')
