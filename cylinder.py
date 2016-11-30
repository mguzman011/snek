#
# cylinder.py
#

from visual import *

def main():
    """ smallest possible example of a vPython simulation """
    color.brown = (0.46,0.28,0.10)
    python = sphere(pos=(-0.25,0,0), radius=0.5, color=color.brown)
    python1 = sphere(pos=(0.25,0,0),radius=0.3, color=color.brown)
    #pythonface = ellipsoid(pos=(0,0,0), length=1.5, height=1, width=1, color = color.brown)
    eye = sphere(pos=(-0.68,0.17,0.15), radius=0.05, color=color.orange, opacity=0.8)
    eye2 = sphere(pos=(-0.68,0.17,-0.15), radius=0.05, color=color.orange)
    eyeball = sphere(pos=(-0.721,0.17,0.15), radius=0.02, color=color.black)
    eyeball2 = sphere(pos=(-0.721,0.17,-0.15), radius=0.02, color=color.black)
    tooth = cone(pos=(-0.70,-0.15,0.08), axis=(-0.02,-0.05, 0), radius=0.025, color=color.white)
    tooth2 = cone(pos=(-0.70,-0.15,-0.08), axis=(-0.02,-0.05, 0), radius=0.025, color=color.white)
    while True:  # time loop!
        rate(10)

# This calls main when the file is run...
if __name__ == "__main__":
    main() 