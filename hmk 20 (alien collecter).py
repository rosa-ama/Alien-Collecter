import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)


pygame.init()


screen_width = 900
screen_height = 600

class Block(pygame.sprite.sprite):
    
    def_init_(self,filename):
    
            super()._init_()

            self.image = pygame.image.load(filename).convert()
            
            self.image.set_colorkey(black)

            self.rect = self.image.get_rect()


    

    
        

pygame.quit()


