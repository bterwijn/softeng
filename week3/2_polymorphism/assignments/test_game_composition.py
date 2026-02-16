import pytest
import softeng
import math

import game_composition as gc

class Screen_Mock:

    def __init__(self, width, height):
        self._width = width
        self._height = height
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height

def test_Random_Start():
    screen = Screen_Mock(800, 600)
    random_start = False
    for i in range(10):
        u = gc.Unit(screen, gc.Position_Random_Start(), gc.Border_Bounce(), color =(255, 0, 0))
        if (math.fabs(u.x - screen.get_width()/2) > 5 or
            math.fabs(u.y - screen.get_height()/2) > 5):
            random_start = True
            break
    assert random_start, "Unit with Random_Start doesn't have random start."

def test_Center_Start():
    screen = Screen_Mock(800, 600)
    center_start = False
    u = gc.Unit(screen, gc.Position_Center_Start(), gc.Border_Bounce(), color =(255, 0, 0))
    if (math.fabs(u.x - screen.get_width()/2) < 2 and
        math.fabs(u.y - screen.get_height()/2) < 2):
        center_start = True
    assert center_start, "Unit with Center_Start doesn't start in center."

def test_Border_Bounce():
    screen = Screen_Mock(800, 600)
    u = gc.Unit(screen, gc.Position_Random_Start(), gc.Border_Bounce(), color =(255, 0, 0))
    u.x = 1
    u.y = 1
    u.dx = -5
    u.dy = 0
    u.step(screen)
    assert u.dx == +5, "Unit with Border_Bounce doesn't bounce on left border."
    u = gc.Unit(screen, gc.Position_Random_Start(), gc.Border_Bounce(), color =(255, 0, 0))
    u.x = 1
    u.y = 1
    u.dx = 0
    u.dy = -5
    u.step(screen)
    assert u.dy == +5, "Unit with Border_Bounce doesn't bounce on top border."

def test_Border_Wraparound():
    screen = Screen_Mock(800, 600)
    u = gc.Unit(screen, gc.Position_Random_Start(), gc.Border_Wraparound(), color =(255, 0, 0))
    u.x = 1
    u.y = 1
    u.dx = -5
    u.dy = 0
    u.step(screen)
    assert u.x > screen.get_width()-10, "Unit with Border_Wraparound doesn't wraparound on left border."
    u = gc.Unit(screen, gc.Position_Random_Start(), gc.Border_Wraparound(), color =(255, 0, 0))
    u.x = 1
    u.y = 1
    u.dx = 0
    u.dy = -5
    u.step(screen)
    assert u.y > screen.get_height()-10, "Unit with Border_Wraparound doesn't wraparound on top border."