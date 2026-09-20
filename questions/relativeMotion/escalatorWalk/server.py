import random
def generate(data):
    stand=random.choice([24,30,36]); walk=random.choice([12,15,18]); moving=1/(1/stand+1/walk); total=walk
    data['params'].update(stand=stand,walk=walk,correct=f'{moving:.1f}',a=f'{stand+walk:.1f}',b=f'{1/(1/stand-1/walk):.1f}',c=f'{stand-walk:.1f}')
