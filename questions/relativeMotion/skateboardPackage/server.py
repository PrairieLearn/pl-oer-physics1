import random, math
def generate(data):
    board=random.choice([8,10,12]); pkg=random.choice([6,8,10]); ang=random.choice([30,45,60]); x=pkg*math.cos(math.radians(ang)); y=pkg*math.sin(math.radians(ang)); speed=math.hypot(board+x,y); direction=math.degrees(math.atan2(y,board+x))
    answers=[round(speed,1),round(board+pkg,1),round(math.hypot(board-x,y),1),round(pkg,1)]
    for i in range(1,4):
        while answers[i] in answers[:i]: answers[i]=round(answers[i]+0.1,1)
    data['params'].update(board=board,pkg=pkg,ang=ang,correct=f'{answers[0]:.1f}',a=f'{answers[1]:.1f}',b=f'{answers[2]:.1f}',c=f'{answers[3]:.1f}',direction=f'{direction:.1f}')
