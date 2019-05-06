"""
Final Project: Snake Game
Author: Sean
Credit: Tutorials

Assignment:
Create an old-school snake game
"""

from ggame import App, RectangleAsset, CircleAsset, Sprite, LineStyle, Color
import math
import random

class Helicopter(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Helicopter.rect, position)
        self.vy = 0
        self.vx = 0
        
        Helicopter.listenKeyEvent("keydown", "up arrow", self.lift)
        Helicopter.listenKeyEvent("keyup", "up arrow", self.fall)
        
    def lift(self, event):
        self.vy += 0.05
        self.deltavy = 0
        
    def fall(self, event):
        self.deltavy = -0.1
        
    def step(self):
        self.y += self.vy
        self.vy += self.deltavy
        
class HelicopterGame(App):
    def __init__(self):
        super().__init__()
        self.player1 = Helicopter((self.width/2, self.height/2))
        
    def step(self):
        self.player1.step()

myapp = HelicopterGame()
myapp.run()