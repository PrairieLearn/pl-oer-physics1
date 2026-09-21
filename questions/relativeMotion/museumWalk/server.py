import random
def generate(data):
    length=random.choice([60,72,84]); stand=random.choice([60,72,90]); walk=random.choice([30,36,45]); moving=1/(1/stand+1/walk)
    data['params'].update(length=length,stand=stand,walk=walk,correct=f'{moving:.1f}',a=f'{stand+walk:.1f}',b=f'{length/(length/stand-length/walk):.1f}',c=f'{length/walk:.1f}')
