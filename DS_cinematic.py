import pygame
pygame.init()
def cam_flipper(img_seq,mode,framecount,display_width,display_height):
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    #render camera flipping animations
    #mode: True: forward False: backward
    for i in range (20):
        if mode:
            gameDisplay.blit((img_seq[i]),(0,0))
        else:
            gameDisplay.blit((img_seq[19-i]),(0,0))
        pygame.display.update()
        framecount+=1
    return framecount

def cinematic_setup(display_width,display_height):
    pass
