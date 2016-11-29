#
# bounce.py
#
# builds from an example that comes with vPython
#   docs: http://vpython.org/contents/docs/index.html
#   gallery of shapes: http://vpython.org/contents/docs/primitives.html
#

from visual import *
import random

def random_color():
    """ returns a tuple of (r,g,b) randomly from 0.0 to 1.0
    """
    r = random.uniform(0.0,1.0)
    g = random.uniform(0.0,1.0)
    b = random.uniform(0.0,1.0)
    return (r,g,b)  # a color is a three-element tuple


def main():
    """ this is the main function, including all of the data objects 
        and the "event loop," which is the while True: loop that will
        become vPython's "time stream" :-)
    """
    # floor
    floor = box(length=4, height=0.5, width=4, pos=(0,0,0), color=(0,0,1))

    # ball
    ball = helix(pos=(0,2,0), axis=(0,3,0), radius=0.5)  # ball is an object of class sphere
    ball.vel = vector(0,-1,0)     # this is its initial velocity

    other = sphere(pos=(1,-2,1), radius=0.5)
    other.vel = vector(0,1,0)
    

    # your other shape here! Use ball as a model...
    # here is the gallery of all of the 3d primitives: 
    #    http://vpython.org/contents/docs/primitives.html


    # other constants
    gravity = 9.8
    RATE = 30                # the number of times the while loop runs each second
    dt = 1.0/(1.0*RATE)      # the time step each time through the while loop
    scene.autoscale = False  # avoids changing the view automatically
    
    while True:    # this is the "physics loop": each loop is one step in time, dt
        rate(RATE) # maximum # of times per second the while loop runs 

        # +++ start of UPDATE SECTION - update all positions here, every time step

        ball.pos = ball.pos + ball.vel*dt
        print("Spring position is:")
        print(ball.pos)
        print("Spring velocity is:")
        print(ball.vel)

        other.pos = other.pos + other.vel*dt

        # +++ end of UPDATE SECTION - be sure new objects are updated appropriately!



        # +++ start of COLLISION SECTION - check for collisions + do the "right" thing

        if ball.y < ball.radius-.25:          # if there is a collision!
            ball.y = ball.radius-.25       # make sure we "uncollide"
            ball.vel.y = -ball.vel.y 
                 # change the sign of the velocity
        else:
            ball.vel.y = ball.vel.y - gravity*dt   # decrease velocity each step
        
        if other.y> other.radius-1.1:          # if there is a collision!
            other.y = other.radius-1.1     # make sure we "uncollide"
            other.vel.y = -other.vel.y 
                 # change the sign of the velocity
        else:
            other.vel.y = other.vel.y + gravity*dt

        # +++ end of COLLISION SECTION



        # +++ start of KEYBOARD SECTION - check for keypresses here + handle them

        if scene.kb.keys: # check if there is an event waiting to be processed?
            k = scene.kb.getkey() # get the key into the variable k
            #print "k is", k
            if k in '=+': gravity *= 1.1
            if k in '-_': gravity *= 0.9
            if k in '-_=+': print "gravity is", gravity

            if k in 'gG': ball.color = (0,1,0) # entirely green (r,g,b) from 0 to 1
            if k in 'rR': ball.color = (1,0,0) # entirely red
            if k in 'nN': ball.color = random_color() # a random color

            if k == 'down': print 'down key'
            if k == 'left': print 'left key'
            if k == 'right': print 'right key'
            if k == 'up': 
                print 'up key'
                ball.vel.z = 3.0
            if k == 'R':  # reset!
                ball.vel = vector(0,-1,0)
                ball.pos = vector(0,2,0)
                ball.color = color.red 
                gravity = 9.8

            # RANDOM COLOR PRESSING C
            if k == 'c': 
                ball.color = random_color()
                other.color = random_color()


        # +++ end of KEYBOARD SECTION - check for keypresses here + handle them


# things start here!
if __name__ == "__main__":
    main()

