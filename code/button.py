import pygame as pg

class Button():
    def __init__(self, img, x, y, width, height, command):
        self.img = pg.transform.scale(img, (width, height))
        self.img.set_colorkey((255, 255, 255))
        self.rect = self.img.get_rect(topleft=(x, y))
        self.command = command

    def draw(self, screen):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        
        if self.rect.collidepoint(mouse):
            screen.blit(self.img, self.rect.topleft)
            if click[0] == 1 and self.command is not None:
                self.command()
        else:
            screen.blit(self.img, self.rect.topleft)

    def set_command(self, command):
        self.command = command
