import random
def generate(data):
    belt=random.choice([0.8,1,1.2]); package=random.choice([1.5,2,2.5]); length=random.choice([24,30,36]); t=length/(belt+package); tstand=length/belt; tback=length/(package-belt)
    answers=[round(t,1),round(tstand,1),round(tback,1),round(length/package,1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.1,1)
    data['params'].update(belt=f'{belt:g}',package=f'{package:g}',length=length,correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}')
