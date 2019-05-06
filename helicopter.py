"""
Final Project: Snake Game
Author: Sean
Credit: Tutorials, Stack Overflow

Assignment:
Create an old-school snake game
"""

from ggame import App, RectangleAsset, CircleAsset, Sprite, LineStyle, Color
import math
import random

class Walls(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(95, 100, noline, black)
    
    def __init__(self, position, speed):
        super().__init__(Walls.rect, position)
        self.vx = -speed
        
    def step(self):
        self.x += self.vx

class Helicopter(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Helicopter.rect, position)
        self.vy = 0
        self.vx = 0
        self.deltavy = 0.1
        
        HelicopterGame.listenKeyEvent("keydown", "up arrow", self.lift)
        HelicopterGame.listenKeyEvent("keyup", "up arrow", self.fall)
        
    def lift(self, event):
        self.vy += -0.12
        self.deltavy = 0
        
    def fall(self, event):
        self.deltavy = 0.08
        
    def step(self):
        self.y += self.vy
        self.vy += self.deltavy
        
class HelicopterGame(App):
    def __init__(self):
        super().__init__()
        self.player1 = Helicopter((self.width/2, self.height/2))
        for x in range(0, self.width//100 + 1):
            
        Walls((self.width - 100, 0),2)
        Walls((self.width - 100, self.height - 100),2)
        
    def step(self):
        self.player1.step()
        for wall in self.getSpritesbyClass(Walls):
            wall.step()
            if wall.x < -100:
                wall.destroy()

myapp = HelicopterGame()
myapp.run()