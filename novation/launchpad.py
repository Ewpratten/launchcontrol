# load launchpad lib
import sys
import pygame
import launchpad_py as launchpad

# init the pygame MIDI controller
pygame.init()

class LaunchpadController(object):
    lp: launchpad.Launchpad

    def __init__(self):
        
        self.lp = launchpad.Launchpad();

    def connect(self):
        if self.lp.Open():
            print("Connected to device")
        else:
            print("Connection fail")

    def flush(self):
        self.lp.ButtonFlush()
        self.lp.Reset()
    
    def disconnect(self):
        self.flush()
        self.lp.Close()

    def setLED(self, x, y, r,g):
        self.lp.LedCtrlXY(x, y, r,g)

    def currentButton(self) -> tuple:
        if self.lp.ButtonChanged():
            rv = self.lp.ButtonStateXY()
            self.lp.ButtonFlush()
            return (rv[0], rv[1])
        else:
            return None