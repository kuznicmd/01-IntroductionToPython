"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Michael Kuznicki.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(10)

alfred = rg.SimpleTurtle('turtle')
alfred.pen_up()
alfred.left(140)
alfred.forward(450)
alfred.right(140)

rachel = rg.SimpleTurtle('arrow')
rachel.pen_up()
rachel.right(40)
rachel.forward(450)
rachel.right(140)

jerry = rg.SimpleTurtle('square')
jerry.pen_up()
jerry.left(40)
jerry.forward(450)
jerry.right(130)

claire = rg.SimpleTurtle('circle')
claire.pen_up()
claire.right(140)
claire.forward(450)
claire.right(130)

alfred.pen = rg.Pen('red', 5)
rachel.pen = rg.Pen('blue', 5)
jerry.pen = rg.Pen('green', 5)
claire.pen = rg.Pen('purple', 5)
alfred.pen_down()
rachel.pen_down()
jerry.pen_down()
claire.pen_down()

distance = 500
alfred.speed = 20

for k in range(10):

    for k in range(4):

        alfred.forward(distance)
        alfred.right(90)

    alfred.pen_up()
    alfred.right(45)
    alfred.forward(50)
    alfred.left(45)
    alfred.pen_down()
    distance = distance - 50

distance = 500
rachel.speed = 20

for k in range(10):

    for k in range(4):

        rachel.forward(distance)
        rachel.right(90)

    rachel.pen_up()
    rachel.right(45)
    rachel.forward(50)
    rachel.left(45)
    rachel.pen_down()
    distance = distance - 50

distance = 500
jerry.speed = 20

for k in range(10):

    for k in range(4):

        jerry.forward(distance)
        jerry.right(90)


    jerry.pen_up()
    jerry.right(45)
    jerry.forward(50)
    jerry.left(45)
    jerry.pen_down()
    distance = distance - 50

distance = 500
claire.speed = 20

for k in range(10):

    for k in range(4):

        claire.forward(distance)
        claire.right(90)


    claire.pen_up()
    claire.right(45)
    claire.forward(50)
    claire.left(45)
    claire.pen_down()
    distance = distance - 50

window.close_on_mouse_click()