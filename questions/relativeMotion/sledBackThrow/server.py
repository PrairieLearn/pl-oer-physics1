import random
def generate(data):
    sled=random.choice([7,9,11]); throw=random.choice([4,5,6]);
    answers=[sled-throw,sled+throw,throw-sled,sled-2*throw]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]+=1
    data['params'].update(sled=sled,throw=throw,correct=answers[0],a=answers[1],b=answers[2],c=answers[3])
