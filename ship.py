import pygame

class Ship():

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # load image as a rectangle

        self.rect.centerx = self.screen_rect.centerx # screen center
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)