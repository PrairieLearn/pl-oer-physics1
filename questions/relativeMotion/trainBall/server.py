import random
def generate(data):
    ball=random.choice([12,15,18,20]); train=random.choice([8,10,12]);
    while ball == train:
        ball=random.choice([12,15,18,20])
    data['params'].update(ball=ball,train=train,forward=ball+train,back=train-ball,absback=abs(train-ball),a=ball-train,b=ball+2*train)
