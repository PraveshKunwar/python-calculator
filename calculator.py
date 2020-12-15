# Welcome! This is a pretty basic calculator that is made with python. This is to help me learn python! Thanks for checking it out!
import divide
import multiply
import add
import sub
import SinCosTan
import log
from Volumes import rectSolid
from Volumes import cube
from Volumes import cylinder
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
    8. Square
    9. Ellipsoid
    10. Tetrahedron 
    """)
    volInput = input()
    if "1" in volInput:
        rectSolid.calc()
    if "2" in volInput: 
        cube.cube()
    if "3" in volInput:
        cylinder.cylinderCalc()

elif getInput != "1" or "2" or "3" "4" or "5" or "6" or "7" or "8" or "9":
    print("Please make sure to enter the correct step!")