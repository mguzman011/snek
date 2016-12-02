#
# cylinder.py
#

from visual import *
import Image

def main():
    """ smallest possible example of a vPython simulation """
    color.brown = (0.46,0.28,0.1)
    python = sphere(pos=(-0.25,0,0),radius=0.5,color = color.brown, material=materials.BlueMarble)
    python1 = sphere(pos=(0.25,0,0),radius=0.3,color = color.brown, material=materials.BlueMarble)
    eye = sphere(pos=(-0.6,0.21,0.2),radius=0.1,color = color.orange)
    eye2 = sphere(pos=(-0.6,0.21,-0.2),radius=0.1,color = color.orange)
    pupil = sphere(pos=(-0.685,0.21,0.24),radius=0.02, color = color.black)
    pupil2 = sphere(pos=(-0.66,0.27,-0.24),radius=0.02,color=color.black)
    tooth = cone(pos=(-0.7,-0.15,0.1),axis=(-0.02,-0.05,0),radius =0.03,color=color.white)
    tooth2 = cone(pos=(-0.7,-0.15,-0.1),axis=(-0.02,-0.05,0),radius = 0.03,color=color.white)
    while True:  # time loop!
        rate(10)

# This calls main when the file is run...
if __name__ == "__main__":
    main() 
