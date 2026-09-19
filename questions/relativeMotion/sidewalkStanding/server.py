import random
def generate(data):
    length=random.choice([48,60,72]); t=random.choice([60,80,90]);
    data['params'].update(length=length,t=t,correct=f'{length/t:.2f}',a=f'{length/(t+10):.2f}',b=f'{length/(t-10):.2f}',c=f'{length/(t+20):.2f}')
