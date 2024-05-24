import unittest
import pygame
import random
from pygame.locals import FULLSCREEN
from meteorite import Meteorite
from os import path

black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((600, 600))
width, height = screen.get_size()
img_dir = path.join(path.dirname(__file__), "img")
snd_dir = path.join(path.dirname(__file__), "snd")
meteo_list = ["m1.png", "m2.png", "m3.png", "m4.png", "m5.png", "m6.png", "m7.png"]

class TestMeteorite(unittest.TestCase):

    def setUp(self):
        self.meteorite = Meteorite()
        self.meteorite.rect.y = -800  # Ensure consistent initial position for testing

    def test_meteorite_initialization(self):
        self.assertIn(self.meteorite.meteochoice, meteo_list)
        self.assertEqual(self.meteorite.meteoriteimg_orig.get_size(), self.meteorite.image.get_size())
        self.assertEqual(self.meteorite.image.get_colorkey(), black)
        self.assertTrue(0 <= self.meteorite.rect.x < width)
        self.assertEqual(self.meteorite.rect.y, -800)
        self.assertTrue(-10 <= self.meteorite.speedx < 10)
        self.assertTrue(3 <= self.meteorite.speedy < 13)
        self.assertEqual(self.meteorite.rot, 0)
        self.assertTrue(-15 <= self.meteorite.rotspeed < 15)

    def test_meteorite_rotation(self):
        initial_rotation = self.meteorite.rot
        self.meteorite.rotate()
        self.assertNotEqual(self.meteorite.rot, initial_rotation)

    def test_meteorite_update_position(self):
        initial_x, initial_y = self.meteorite.rect.x, self.meteorite.rect.y
        self.meteorite.update()
        self.assertNotEqual((self.meteorite.rect.x, self.meteorite.rect.y), (initial_x, initial_y))

    def test_meteorite_repositioning(self):
        self.meteorite.rect.right = -1  # Simulate meteorite moving off the left edge of the screen
        self.meteorite.update()
        self.assertTrue(0 <= self.meteorite.rect.x < width)
        self.assertEqual(self.meteorite.rect.y, -500)

if __name__ == "__main__":
    unittest.main()
