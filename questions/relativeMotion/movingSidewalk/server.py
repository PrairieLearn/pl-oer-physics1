import random
def generate(data):
    walk=random.choice([1,1.5,2]); belt=random.choice([0.5,1,1.5]); length=random.choice([48,60,72]);
    t=length/(walk+belt)
    answers=[round(t,1), round(length/walk,1), round(length/(walk+2*belt),1), round(length/(2*walk+belt),1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.1,1)
    data['params'].update(walk=f'{walk:g}',belt=f'{belt:g}',length=length,correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}')
