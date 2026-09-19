import random
def generate(data):
    belt=random.choice([0.5,0.75,1]); length=random.choice([40,54,64]); t=random.choice([80,90,100]);
    stand=length/t; walk=stand+belt; no_belt=length/walk
    answers=[round(no_belt,1), round(t,1), round(t+10,1), round(t/3,1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+1,1)
    data['params'].update(belt=f'{belt:g}',length=length,t=t,correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}')
