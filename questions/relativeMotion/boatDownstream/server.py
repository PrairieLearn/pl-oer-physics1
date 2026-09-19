import random
def generate(data):
    boat=random.choice([4,5,6,7]); current=random.choice([1,2,3]);
    data['params'].update(boat=boat,current=current,correct=boat+current,a=boat-current,b=boat*current,c=boat+current+1)
