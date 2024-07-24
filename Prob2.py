
from pgl import GWindow, GRect, GLabel
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
SHRINK_RATE = 4                     # Rate at which the box dimensions should shrink

def clicky_box():

    # Defining the callback function, which you won't need until Part 3
    def on_mouse_down(event):
        print("You clicked the window!") # Delete this once you start Part C

    # Defining the timer callback function, which you won't need until part 5
    def animate():
        print("I'm called!")


    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT)












if __name__ == '__main__':
    clicky_box()
