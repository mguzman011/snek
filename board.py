#
# board.py
# Name: Michael Guzman, Shruthi Sukir, Emily Zhao
#

from visual import *
import random

def make_snek():
    snek = frame( pos=(0,0,0) )
    color.brown = (0.46,0.28,0.1)
    python = sphere(frame = snek, pos=(-0.5,0,0), radius = 1, color = color.brown, material=materials.BlueMarble)
    #python1 = sphere(frame = snek, pos=(0.5,0,0),radius=.6, color = color.brown, material=materials.BlueMarble)
    #eye = sphere(frame = snek, pos=(-1.2,0.42,0.4),radius=0.2,color = color.orange)
    #eye2 = sphere(frame = snek, pos=(-1.2,0.42,-0.4),radius=0.2,color = color.orange)
    #pupil = sphere(frame = snek, pos=(-1.37,0.42,0.48),radius=0.04, color = color.black)
    #pupil2 = sphere(frame = snek, pos=(-1.32,0.54,-0.48),radius=0.04,color=color.black)
    #tooth = cone(frame = snek, pos=(-1.4,-0.3,0.2),axis=(-0.02,-0.05,0),radius =0.06,color=color.white)
    #tooth2 = cone(frame = snek, pos=(-1.4,-0.3,-0.2),axis=(-0.02,-0.05,0),radius = 0.06,color=color.white)
    return snek

def make_walls():
    """ makes several walls and returns them in a list
    """
    w0 = box(pos=(-20,0,0), axis=(0,0,1), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w1 = box(pos=(0,0,-20), axis=(1,0,0), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w2 = box(pos=(0,0,20), axis=(1,0,0), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w3 = box(pos=(20,0,0), axis=(0,0,1), length=40, width=1, height = 2, color=color.red, material=materials.wood)
    list_of_walls = [ w0, w1 , w2, w3]
    return list_of_walls

def main():
    """ this is the main function, including all of the data objects and the "event loop" which is the while True: loop that will be the universe's "time stream" :-)
    """
    scene = display(title='Game',x=0, y=0, width=1000, height=700,center=(0,0,0), background=(0,0,0), forward=(0,-2,0), userzoom=False, userspin=False) #camera move
    # create an object named floor of class (type) box:
    floor = box(pos=(0,-1,0), length=40, width=40, height = 0.5, color=color.white)

    # this creates a list of walls 
    Walls = make_walls()
    w0, w1, w2, w3 = Walls   # and gives each one a name...

    snek = make_snek()
    snek.vel = vector(0,0,0)

    # We set some variables to control the display and the event loop
    RATE = 30             # number of loops per second to run, if possible!
    dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
    autocenter = True     # do you want vPython to keep the scene centered?

    # Make a pellet
    pelletposx = random.randint(-18,18)
    pelletposz = random.randint(-18,18)
    pellet = sphere(radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white)
    bodypos = 1
    bodycount = 0

    # Scoring
    score = 0
    scorelbl = label(pos = (-18,24,0), text='Score: %d'%score, box = False)

    # Game Over
    def reset():
        gameover = text(text='GAME OVER',font='comic sans',depth=-1,height=4,width=2,color=color.red,pos=(0,0,-10),axis=(.10,0,0),align='center')
        sleep(2)
        snek.vel = vector(0,0,0)
        snek.pos = vector(0,0,0)
        gameover.visible = False
        score = 0
        scorelbl = label(pos = (-18,24,0), text='Score: %d'%score, box = False)


    # this is the main loop of the program! it's "time" or the "event loop"
    while True:
        rate(RATE)     # run no faster than RATE loops/second

        # +++++ start of all position updates: once per loop +++++ 

        snek.pos = snek.pos + snek.vel

        # +++++ end of all once-per-loop position updates +++++ 


        # ----- start of other checks - especially *collisions* -----
        #pellet collision
        vec_from_pellet_to_snek = pellet.pos-snek.pos
        if mag(vec_from_pellet_to_snek) < 2:
            score += 1
            scorelbl = label(pos = (-18,24,0), text='Score: %d'%score, box = False)
            pellet.visible = False
            pelletposx = random.randint(-18,18)
            pelletposz = random.randint(-18,18)
            pellet = sphere(radius = 0.5, pos = (pelletposx, 0 , pelletposz), color = color.white)
            #body handling
            #body = sphere(frame = snek, pos=(bodypos,0,0), radius=.6 , color = color.brown, material=materials.BlueMarble)
            #bodycount += 1
            #bodypos += 1   


 
                
        # colliding with wall 0, w0:
        if snek.pos.x < w0.pos.x+1.5:  # w0 has the smallest x value
            snek.pos.x = w0.pos.x+1.5  # make sure we stay in bounds
            snek.vel.x = 0   # bounce (in the x direction)
            reset()
        # colliding with wall 1, w1:
        if snek.pos.z < w1.pos.z+1.5:  # w1 has the smallest z value
            snek.pos.z = w1.pos.z+1.5  # make sure we stay in bounds
            snek.vel.z = 0   # bounce (in the x direction)
            reset()
         # colliding with wall 0, w0:
        if snek.pos.x > w2.pos.x +18.5:  # w2 has the largest x value
            snek.pos.x = w2.pos.x +18.5  # make sure we stay in bounds
            snek.vel.x = 0   # bounce (in the x direction)
            reset()
        # colliding with wall 0, w0:

        if snek.pos.z > w3.pos.z + 18.5:  # w3 has the largest x value
            snek.pos.z = w3.pos.z + 18.5  # make sure we stay in bounds
            snek.vel.z = 0   # bounce (in the x direction)
            reset()

        # ----- end of other checks - especially *collisions*  -----


        # ===== handling user events: keypresses and mouse =====

        # here, we see if the user has pressed any keys, cannot move backwards
        if scene.kb.keys:   
            s = scene.kb.getkey() 
            dx = .5; dz = .5
            if snek.vel == vector(dx,0,0):
                if s == 'up': snek.vel = vector(0,0,-dz)
                if s == 'down': snek.vel = vector(0,0,dz)
            elif snek.vel == vector(-dx,0,0):
                if s == 'up': snek.vel = vector(0,0,-dz)
                if s == 'down': snek.vel = vector(0,0,dz)
            elif snek.vel == vector(0,0,dz):
                if s == 'left': snek.vel = vector(-dx,0,0)
                if s == 'right': snek.vel = vector(dx,0,0)
            elif snek.vel == vector(0,0,-dz):
                if s == 'left': snek.vel = vector(-dx,0,0)
                if s == 'right': snek.vel = vector(dx,0,0)
            else:
                if s == 'up': snek.vel = vector(0,0,-dz)
                if s == 'down': snek.vel = vector(0,0,dz)
                if s == 'left': snek.vel = vector(-dx,0,0)
                if s == 'right': snek.vel = vector(dx,0,0)

            # space to stop everything
            if s == ' ':  # space to stop things
                snek.vel = vector (0,0,0)

            # capital R to reset things
            if s == 'R':
                snek.vel = vector(0,0,0)
                snek.pos = vector(0,0,0)

            if s == 'Q':  # Quit!
                print "Quitting..."
                break  # breaks out of the main loop

    print "Done with the main loop. Ending this vPython session..."
    print "Close the vPython window to finish."
# this ends the main() function - it tends to get large!


# This should be the FINAL thing in the file...
#c:\Python27\python board.py
if __name__ == "__main__":   # did we just RUN this file?
    main() # if so, we call main()
