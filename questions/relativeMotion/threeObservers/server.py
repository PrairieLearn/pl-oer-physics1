import random
def generate(data):
    ab=random.choice([2,3,4]); bc=random.choice([5,6,7]); ac=bc-ab
    data['params'].update(ab=ab,bc=bc,correct=ac,a=ab+bc,b=abs(ab-bc),c=bc)
