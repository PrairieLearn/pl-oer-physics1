import random
def generate(data):
    train=random.choice([10,12,15]); ball=random.choice([8,10,12]);
    while ball == train:
        ball=random.choice([8,10,12])
    data['params'].update(train=train,ball=ball,correct=train-ball,a=train+ball,b=ball-train,c=train+2*ball)
