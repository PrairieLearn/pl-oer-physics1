import random
def generate(data):
    belt=random.choice([0.8,1,1.2]); runner=random.choice([1.5,2,2.5]); length=random.choice([30,40,50]); t=length/(runner+belt)
    answers=[round(t,1),round(length/runner,1),round(length/belt,1),round(length/(runner+belt+0.7),1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.1,1)
    data['params'].update(belt=f'{belt:g}',runner=f'{runner:g}',length=length,correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}')
