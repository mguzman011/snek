#
# cylinder.py
#

from visual import *
import Image

def main():
    """ smallest possible example of a vPython simulation """
    color.brown = (0.46,0.28,0.1)
    python = sphere(pos=(-0.5,0,0),radius=1,color = color.brown, material=materials.BlueMarble)
    python1 = sphere(pos=(0.5,0,0),radius=.6,color = color.brown, material=materials.BlueMarble)
    eye = sphere(pos=(-1.2,0.42,0.4),radius=0.2,color = color.orange)
    eye2 = sphere(pos=(-1.2,0.42,-0.4),radius=0.2,color = color.orange)
    pupil = sphere(pos=(-1.37,0.42,0.48),radius=0.04, color = color.black)
    pupil2 = sphere(pos=(-1.32,0.54,-0.48),radius=0.04,color=color.black)
    tooth = cone(pos=(-1.4,-0.3,0.2),axis=(-0.02,-0.05,0),radius =0.06,color=color.white)
    tooth2 = cone(pos=(-1.4,-0.3,-0.2),axis=(-0.02,-0.05,0),radius = 0.06,color=color.white)
    while True:  # time loop!
        rate(10)

# This calls main when the file is run...
if __name__ == "__main__":
    main() 
