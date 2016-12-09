from visual import *
import random



def main():
    count = 1
    scene = display(title='Game',x=0, y=0, width=1000, height=1000,center=(0,0,2), background=(0,0,0), forward=(0,-5,0), userzoom=False, userspin=False)
    floor = box(pos=(0,-1,0), length=40, width=40, height = 0.5, color=color.white)
    RATE = 10             
    autocenter = True 
    #Walls
    w0 = box(pos=(-20,0,0), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w1 = box(pos=(0,0,-20), axis=(1,0,0), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w2 = box(pos=(0,0,20), axis=(1,0,0), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w3 = box(pos=(20,0,0), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    pelletposx = random.randint(-18, 18)
    pelletposz = random.randint(-18,18)
    pellet = sphere( radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white )
    while count == 1:
        L = range(1,2)
        score = 0
        vel = vector(0,0,0)
        snek = []
        snekframe = frame(axis=(1,0,0))
        snek.append(snekframe)
        color.brown = (0.46,0.28,0.1)
        python = sphere(frame = snek[0], pos=(1,0,0), radius = 1, color = color.brown, material=materials.BlueMarble)
        python2 = sphere(pos=(0,0,0),radius = .6,color = color.brown, material=materials.BlueMarble)
        snek.append(python2)
        scorelbl = label(pos = (-18,24,0), text='Score: %d'%score, box = False)
        def follow():
            for i in L[::-1]:
                snek[i].pos=snek[i-1].pos
        def addBody():
            snek.append(sphere(pos=snek[len(snek)-1].pos,radius=.6, color = color.brown, material=materials.BlueMarble))
            L.append(len(L)+1)
        def reset():
            gameover = text(text='GAME OVER',font='comic sans',depth=.0005,height=4,width=2,color=color.red,pos=(0,0,-10),axis=(1,0,0),align='center')
            gameover.rotate(angle=pi/4, axis=(-1,0,0))
            vel = vector(0,0,0)
            sleep(2)
            gameover.visible = False
            score = 0
            scorelbl = label(pos = (-18,24,0), text='Score: %d'%score, box = False)
        while True:
            rate(RATE)
            snek[0].pos = snek[0].pos + vel
            if (snek[0].pos+vel).x < w0.pos.x+1:  # w0 has the smallest x value  
                follow()
                python.visible = False
                for i in L[::-1]:
                    snek[i].visible=False
                reset()
                count = 0
                break
            if (snek[0].pos+vel).z < w1.pos.z+1:  # w1 has the smallest z value 
                follow()
                python.visible = False
                for i in L[::-1]:
                    snek[i].visible=False
                reset()
                count = 0
                break
            if (snek[0].pos+vel).x > w2.pos.x +18:  # w0 has the smallest x value
                follow()
                python.visible = False
                for i in L[::-1]:
                    snek[i].visible=False
                reset()
                count = 0
                break
            if (snek[0].pos+vel).z > w3.pos.z+18:  # w0 has the smallest x value  
                follow()
                python.visible = False
                for i in L[::-1]:
                    snek[i].visible=False
                reset() 
                count = 0 
                break
            follow()
            snekpellet = abs(snek[0].pos - pellet.pos)
            if snekpellet < 1:
                addBody()
                pellet.visible = False
                pelletposx = random.randint(-18, 18)
                pelletposz = random.randint(-18,18)
                pellet = sphere( radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white )
                score+=1
                scorelbl.text='Score: %d'%score
            if scene.kb.keys:
                s = scene.kb.getkey()
                dx = 1; dz = 1
                if s == 'left': 
                    if vel == vector(-dx,0,0):
                        pass
                    elif vel == vector(dx,0,0):
                        vel = vector(dx,0,0)
                    else:
                        vel = vector(-dx,0,0)
                        snek[0].axis=vel
                elif s == 'right': 
                    if vel == vector(dx,0,0):
                        pass
                    elif vel == vector(-dx,0,0):
                        vel == vector(-dx,0,0)
                    else:
                        vel = vector(dx,0,0)
                        snek[0].axis=vel
                elif s == 'up': 
                    if vel == vector(0,0,-dz):
                        pass
                    elif vel == vector(0,0,dz):
                        vel == vector(0,0,dz)
                    else:
                        vel = vector(0,0,-dz)
                        snek[0].axis=vel
                elif s == 'down': 
                    if vel == vector(0,0,dz):
                        pass
                    elif vel == vector(0,0,-dz):
                        vel = vector(0,0,-dz)
                    else:
                        vel = vector(0,0,dz)
                        snek[0].axis=vel
                elif s == 'r':
                    gameover = text(text='GAME OVER',font='comic sans',depth=.0005,height=4,width=2,color=color.red,pos=(0,0,-10),axis=(1,0,0),align='center')
                    gameover.rotate(angle=pi/4, axis=(-1,0,0))
                    vel = vector(0,0,0)
                    sleep(2)
                    gameover.visible = False
                    python.pos = (1,0,0)
                    python2.pos = (0,0,0)
                    score = 0
                    scorelbl = label(pos = (-18,24,0), text='Score: %d'%score, box = False)
        count = 1
if __name__ == "__main__":  
    main()                  


