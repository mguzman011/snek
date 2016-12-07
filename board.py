#
# billiard_bounce.py
#
# starting file for the game in Lab 11 (hw11pr1.zip)
#
# If you enjoy vPython, you might consider it as a final project...
#   docs: http://vpython.org/contents/docs/index.html
#   gallery of shapes: http://vpython.org/contents/docs/primitives.html
#
# Name:
#

from visual import *
import random

def make_snek():
    """ smallest possible example of a vPython simulation """
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
    w0 = box(pos=(-20,0,0), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w1 = box(pos=(0,0,-20), axis=(1,0,0), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w2 = box(pos=(0,0,20), axis=(1,0,0), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    w3 = box(pos=(20,0,0), axis=(0,0,1), 
             length=40, width=1, height = 2, color=color.red, material=materials.wood)
    #w4 = box(pos = (-15, 0, 0), axis = (1,0,0), length = 10, width = 1, height = 2, color = color.red, material = materials.wood)
    list_of_walls = [ w0, w1 , w2, w3] #add w4 here if we want more walls
    return list_of_walls


"""def make_alien():
    makes an alien! -- in the process, this shows how to
        group many objects into a single coordinate system ("frame")
        and treat that as a single object
    
    alien = frame( pos=(10,0,-10) )  # makes a new "frame" == a container
    # with a local coordinate system that can have any number of parts...
    # here are the "parts":
    sphere( frame=alien, radius=1, color=color.green )
    sphere( frame=alien, radius=0.3, pos=(.7,.5,.2), color=color.white )
    sphere( frame=alien, radius=0.3, pos=(.2,.5,.7), color=color.white )
    cylinder( frame=alien, pos=(0,.9,-.2), axis=(.02,.2,-.02),  # the hat!
              radius=.7, color=color.magenta)
    return alien   # always use the _frame_, not any of its parts..."""


def main():
    """ this is the main function, including
        all of the data objects and the "event loop"
        which is the while True: loop that will
        be the universe's "time stream" :-)
    """
    scene = display(title='Game',x=0, y=0, width=1000, height=1000,center=(0,0,0), background=(0,0,0), forward=(0,-2,-1), userzoom=False, userspin=False) #camera move
    # create an object named floor of class (type) box:
    floor = box(pos=(0,-1,0), length=40, width=40, height = 0.5, color=color.white)

    # this creates a list of walls 
    Walls = make_walls()
    w0, w1, w2, w3 = Walls   # add w4 here if you want the fourth wall

    # this creates an alien!  (it's a vPython frame)
    #alien = make_alien()
    #alien.vel = vector(0,0,0)  # no velocity (yet!)

    # color names? they are black, blue, cyan, green, gray(v), 0.0<=v<=1.0
    #                       magenta, orange, red, white, yellow
    # or you can use rgb tuples (from 0.0 to 1.0, not 0 to 255), e.g.,
    #ball = sphere( radius=1, pos=(10,0,0), color=(1,0.7,0.2) )
    #ball.vel = vector(0,0,0)   # this is the "game piece" w/ zero starting vel.

    snek = make_snek()
    snek.vel = vector(0,0,0)

    # We set some variables to control the display and the event loop
    RATE = 30             # number of loops per second to run, if possible!
    dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
    autocenter = True     # do you want vPython to keep the scene centered?

    #make a pellet
    pelletposx = random.randint(-18, 18)
    pelletposz = random.randint(-18,18)
    pellet = sphere( radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white )
    bodypos = 1
    bodycount = []
    score = 0


    # this is the main loop of the program! it's "time" or the "event loop"
    while True:
        rate(RATE)     # run no faster than RATE loops/second

        # +++++ start of all position updates: once per loop +++++ 

        #ball.pos = ball.pos + ball.vel*dt           # PHYSICS!
        #alien.pos = alien.pos + alien.vel*dt
        snek.pos = snek.pos + snek.vel
        #print(angle.diff_angle(snek.pos)*pi/180)

        body = sphere(pos=(snek.pos.x+1,snek.pos.y,snek.pos.z), radius=.6 , color = color.brown, material=materials.BlueMarble)
        body.vel = snek.vel
        body.pos = body.pos + body.vel

        # +++++ end of all once-per-loop position updates +++++ 


        # ----- start of other checks - especially *collisions* -----

        # collision check for the ball and alien...
        # vector docs:   http://vpython.org/contents/docs/vector.html
        vec_from_pellet_to_snek = pellet.pos-snek.pos
        if mag(vec_from_pellet_to_snek) < 1.5:
            pellet.visible = False
            pelletposx = random.randint(-18, 18)
            pelletposz = random.randint(-18,18)
            pellet = sphere( radius=0.5, pos=(pelletposx,0,pelletposz), color = color.white )
            body = sphere(pos=(snek.pos.x+1,snek.pos.y,snek.pos.z), radius=.6 , color = color.brown, material=materials.BlueMarble)
            body.vel = snek.vel
            body.pos = body.pos + body.vel
            bodycount.append(body.pos)
            score += 1
            bodypos += 1 
            print(score)
            print (bodycount)       

        #vec_from_ball_to_alien = alien.pos - snek.pos
        #if mag( vec_from_ball_to_alien ) < ball.radius:
            #print "You've freed the alien! Going home..."
            #alien.vel = vector(0,5,0)
        
        # need to handle wall collisions next...
        # here is an example of one wall collision - you'll need more!
        
        # colliding with wall 0, w0:
        if snek.pos.x < w0.pos.x+1.5:  # w0 has the smallest x value
            snek.pos.x = w0.pos.x+1.5  # make sure we stay in bounds
            snek.vel.x = 0   # bounce (in the x direction)
            print("You ded")
            exit()
        if snek.pos.z < w1.pos.z+1.5:  # w1 has the smallest z value
            snek.pos.z = w1.pos.z+1.5  # make sure we stay in bounds
            snek.vel.z = 0   # bounce (in the x direction)
            print("You died")
            exit()
        if snek.pos.x > w2.pos.x +18.5:  # w0 has the smallest x value
            snek.pos.x = w2.pos.x +18.5  # make sure we stay in bounds
            snek.vel.x = 0   # bounce (in the x direction)
            print("You dieded")
            exit()
        if snek.pos.z > w3.pos.z+18.5:  # w0 has the smallest x value
            snek.pos.z = w3.pos.z+18.5  # make sure we stay in bounds
            snek.vel.z = 0   # bounce (in the x direction)
            print("You dedderino")
            exit() 

        """if snek.pos.x =< w4.pos.x+6 and w4.pos.z-1.5<=snek.pos.z=<w4.posz+1.5:  # w0 has the smallest x value
            snek.pos.x = w4.pos.x-1  # make sure we stay in bounds
            snek.pos.z = snek.pos.z-1.5
            snek.vel.x = -1.0 * snek.vel.x   # bounce (in the x direction)
            snek.vel.z = -1.0 * snek.vel.z"""

        # ----- end of other checks - especially *collisions*  -----




        # ===== handling user events: keypresses and mouse =====

        # here, we see if the user has pressed any keys
        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            #print "You pressed the key", s  

            # Key presses to give the ball velocity (in the x-z plane)
            dx = .5; dz = .5   # easily-changeable values
            if s == 'left': 
                snek.vel = vector(-dx,0,0)
                #rotation = snek.rotate(angle = pi/2, axis = (0,1,0), orgin = snek.pos)
            if s == 'right': 
                snek.vel = vector(dx,0,0)
            if s == 'up': 
                snek.vel = vector(0,0,-dz)
            if s == 'down': 
                snek.vel = vector(0,0,dz)

            # space to stop everything
            if s == ' ':  # space to stop things
                #ball.vel = vector(0,0,0)
                #alien.vel = vector(0,0,0)
                snek.vel = vector (0,0,0)

            # capital R to reset things
            if s == 'R':
                #ball.vel = vector(0,0,0)
                #ball.pos = vector(10,0,0)
                #alien.vel = vector(0,0,0)
                #alien.pos = vector(-10,0,random.uniform(-10,10))
                snek.vel = vector(0,0,0)
                snek.pos = vector(0,0,0)

            if s == 'Q':  # Quit!
                print "Quitting..."
                break  # breaks out of the main loop

            # mouse is better handled only when a particular key is pressed
            # see http://vpython.org/contents/docs/mouse.html for more

        # ===== end of handling user events: keypresses and mouse =====

    print "Done with the main loop. Ending this vPython session..."
    print "Close the vPython window to finish."
# this ends the main() function - it tends to get large!


# This should be the FINAL thing in the file...
if __name__ == "__main__":   # did we just RUN this file?
    main()                   # if so, we call main()







