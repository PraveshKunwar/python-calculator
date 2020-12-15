# Welcome! This is a pretty basic calculator that is made with python. This is to help me learn python! Thanks for checking it out!
import divide
import multiply
import add
import sub
import SinCosTan
import log
from Misc import exponent
from Misc import quadratic
from Misc import slope
from Misc import interest
from Volumes import rectSolid
from Volumes import cube
from Volumes import cylinder
from Volumes import prism
from Volumes import sphere
from Volumes import pyramid
from Volumes import rcc
from Volumes import recPyramid
from Volumes import tetrahedron
print(
    """What would you like to do today?
    1. Add
    2. Sub
    3. Multiply
    4. Divide
    5. Sin
    6. Cos
    7. Tan
    8. Log
    9. Volumes of Shapes
    00. Additional Features
    To choose what you would like, just type the number of the calculation!
    """
)  #This is where the user will enter the statement that they want to calculate
getInput = input()

if "1" in getInput: 
    add.add()

if "2" in getInput: 
    sub.sub()

if "3" in getInput:
    multiply.multiply()

if "4" in getInput:
    divide.divide()

if "5" in getInput:
    SinCosTan.Sin()

if "6" in getInput:
    SinCosTan.Cos()

if "7" in getInput:
    SinCosTan.Tan()

if "8" in getInput: 
    log.log()

if "9" in getInput:
    print("""
    Which volume would you like to calculate? 
    1. Rectangular Solid
    2. Cube
    3. Cylinder
    4. Prism
    5. Sphere
    6. Pyramid
    7. Right Cylandrical Cone
    8. Rectangular Pyramid
    9. Tetrahedron 
    """)
    volInput = input()
    if "1" in volInput:
        rectSolid.calc()
    if "2" in volInput: 
        cube.cube()
    if "3" in volInput:
        cylinder.cylinderCalc()
    if "4" in volInput:
        prism.prismCalc()
    if "5" in volInput: 
        sphere.sphereCalc()
    if "6" in volInput: 
        pyramid.pyrmaidCalc()
    if "7" in volInput:
        rcc.rccCalc()
    if "8" in volInput: 
        recPyramid.recPyrmaidCalc()
    if "9" in volInput:
        tetrahedron.tetraherdonCalc()

elif getInput != "1" or "2" or "3" "4" or "5" or "6" or "7" or "8" or "9" or "10":
    print("Please make sure to enter the correct step!")

if "00" in getInput:
   print("""
   Additional Features:
   1. Exponent
   2. Quadratic
   3. Slope/Equation/B intercept
   4. Interest
   """)
   additionalInput = input()
   if "1" in additionalInput:
       exponent.exponent()
   if "2" in additionalInput:
    quadratic.quadraticCalc()
   if "3" in additionalInput: 
    slope.slopeCalc()
   if "4" in additionalInput:
       interest.interest()
