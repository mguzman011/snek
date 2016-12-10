from visual import *
import random

def main():
    """this is the main function, including all of the data objects and the "event loop" which is the while True: loop that will be the universe's "time stream" :)
    """

    # def menu():
    #     """ makes a main menu.
    #     """
    #     first = frame(pos=(0,0,0))
    #     test = box(frame=first, pos=(0,0,0), length=42, width=42, height=5, color=color.black)
    #     intro = text(text='PYTHON',font='comic sans',depth=.0005,height=4,width=2,color=color.red,pos=(0,20,0),axis=(1,0,0),align='center')
    #     intro.rotate(angle=pi/4, axis=(-1,0,0))
    #     # scorelbl.visible = False
    #     if scene.kb.keys:   
    #         s = scene.kb.getkey() 
    #         if s == 'p':
    #             menu.visible = False
    #     return first

    # Creates Scene (camera, walls, floor)
    scene = display(title='Game',x=0, y=0, width=1000, height=1000,center=(0,0,2), background=(0,0,0), forward=(0,-5,0), userzoom=False, userspin=False) #camera move
    # menu()
    
    # create an object named floor of class (type) box:
    floor = box(pos=(0,-1,0), length=40, width=40, height = 0.5, color=color.white)

    #walls
    w0 = box(pos=(-20,0,0), axis=(0,0,1), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w1 = box(pos=(0,0,-20), axis=(1,0,0), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w2 = box(pos=(0,0,20), axis=(1,0,0), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w3 = box(pos=(20,0,0), axis=(0,0,1), length=40, width=1, height = 2, color=color.red, material=materials.wood)

    #setup snek
    RATE = 10
    snek = []
    snekframe = frame(axis=(1,0,0))
    snek.append(snekframe)
    color.brown = (0.46,0.28,0.1)
    python = sphere(frame = snek[0], pos=(1,0,0), radius = 1, color = color.brown, material=materials.BlueMarble)
    snek.append(sphere(pos=(0,0,0),radius = .6,color = color.brown, material = materials.BlueMarble))
    bodycount = 1
    snekvel = vector(0,0,0)
    snekpos = vector(0,0,0)
    L = range(1,2)

    # title screen
    intro = box(pos=(0,0,0), length=42, width=42, height=5, color=color.black)
    title = text(text='PYTHON',font='comic sans',depth=.0005,height=4,width=2,color=color.red,pos=(0,20,0),axis=(1,0,0),align='center')
    title.rotate(angle=pi/4, axis=(-1,0,0))
    inst = text(text='Press Enter to Start',font='comic sans',depth=.0005,height=1,width=1,color=color.green,pos=(0,20,5),axis=(1,0,0),align='center')
    inst.rotate(angle=pi/4, axis=(-.81,0,0))
    

    #setup score
    score = 0
    scorelbl=label(pos=(-15,24,-10),text='score: %d'%score,box=False,visible=False)



    def reset():
        """resets the program; puts a Game Over sign, waits, then resets the board and the score
        """
        gameover = text(text='GAME OVER',font='comic sans',depth=.0005,height=4,width=2,color=color.red,pos=(0,0,-10),axis=(1,0,0),align='center')
        gameover.rotate(angle=pi/4, axis=(-1,0,0))
        # sleep(2)      
        snekvel = vector(0,0,0)
        #snekpos = vector(0,0,0)
        gameover.visible = False
        score = 0
        scorelbl = label(pos = (-15,24,-10), text='Score: %d'%score, box = False)

    def follow():
        """ makes each new piece of the snake follow the head
        """
        for i in L[::-1]:
            snek[i].pos=snek[i-1].pos
            if snek[i].pos == snek[i-1].pos:
                exit

    #creating pellets
    pelletposx = random.randint(-18, 18)
    pelletposz = random.randint(-18,18)
    pellet = sphere(radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white)

    def addBody():
        """ adds a new piece to the snake each time a pellet is eaten
        """
        snek.append(sphere(pos=snek[len(snek)-1].pos,radius=.6, color = color.brown, material=materials.BlueMarble))
        L.append(len(L)+1)

    # Crashes into wall
    while True:
        rate(RATE)
        snek[0].pos = snek[0].pos + snekvel
        if snek[0].pos.x < w0.pos.x+1.5:  # w0 has the smallest x value
            # follow()
            # python.visible = False
            # for i in L[::-1]:
            #     snek[i].visible=False
            # reset()
            # count = 0
            # break
            exit()
        # colliding with wall 1, w1:
        if snek[0].pos.z < w1.pos.z+1.5:  # w1 has the smallest z value
            # follow()
            # python.visible = False
            # for i in L[::-1]:
            #     snek[i].visible=False
            # reset()
            # count = 0
            # break
            exit()
         # colliding with wall 0, w0:
        if snek[0].pos.x > w2.pos.x +18.5:  # w2 has the largest x value
            # follow()
            # python.visible = False
            # for i in L[::-1]:
            #     snek[i].visible=False
            # reset()
            # count = 0
            # break
            exit()
        # colliding with wall 0, w0:
        if snek[0].pos.z > w3.pos.z + 18.5:  # w3 has the largest x value
            # follow()
            # python.visible = False
            # for i in L[::-1]:
            #     snek[i].visible=False
            # reset()
            # count = 0
            # break
            exit()
        # if (snek[0].pos+snekvel).x < w0.pos.x+0.5:  # w0 has the smallest x value  
        #     break
        # if (snek[0].pos+snekvel).z < w1.pos.z+0.5:  # w1 has the smallest z value 
        #     break
        # if (snek[0].pos+snekvel).x > w2.pos.x +18.5:  # w2 has the largest x value
        #     break
        # if (snek[0].pos+snekvel).z > w3.pos.z+18.5:  # w3 has the largest z value  
        #     break 
        # for i in range(1,len(snek)):
        #     if snek[0].pos==snek[i].pos:
        #         break
        follow()

        # When pellet is eaten, add to body, add to score, 
        snekpellet = abs(snek[0].pos - pellet.pos)
        if snekpellet < 1:
            addBody()
            pellet.visible = False
            pelletposx = random.randint(-18, 18)
            pelletposz = random.randint(-18,18)
            pellet = sphere( radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white )
            score+=1
            scorelbl.text='score: %d'%score
        
        #key presses
        if scene.kb.keys:
            s = scene.kb.getkey()
            dx = 1; dz = 1
            if s == '\n':
                intro.visible = False
                title.visible = False
                inst.visible = False
                scorelbl.visible = True

                # scorelbl.visible = False
            if snekvel == vector(dx,0,0):
                if s == 'up': snekvel = vector(0,0,-dz)
                if s == 'down': snekvel = vector(0,0,dz)
                snek[0].axis=snekvel
            elif snekvel == vector(-dx,0,0):
                if s == 'up': snekvel = vector(0,0,-dz)
                if s == 'down': snekvel = vector(0,0,dz)
                snek[0].axis=snekvel
            elif snekvel == vector(0,0,dz):
                if s == 'left': snekvel = vector(-dx,0,0)
                if s == 'right': snekvel = vector(dx,0,0)
                snek[0].axis=snekvel
            elif snekvel == vector(0,0,-dz):
                if s == 'left': snekvel = vector(-dx,0,0)
                if s == 'right': snekvel = vector(dx,0,0)
                snek[0].axis=snekvel
            else:
                if s == 'up': snekvel = vector(0,0,-dz)
                if s == 'down': snekvel = vector(0,0,dz)
                if s == 'left': snekvel = vector(-dx,0,0)
                if s == 'right': snekvel = vector(dx,0,0)
                snek[0].axis=snekvel

# This should be the FINAL thing in the file...
#c:\Python27\python Python.py
if __name__ == "__main__":   # did we just RUN this file?
    main() # if so, we call main()

