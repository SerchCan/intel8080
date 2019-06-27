import pygame;
import numpy as np
from Memoria import Memory
class Screen():
    def __init__(self):
        pygame.init()
        self.matrix=None
        self.size = width, height = 256,224
        self.BLACK = 0,0,0
        self.WHITE = 255,255,255
        self.b=True
        self.Screen = pygame.display.set_mode(self.size)
#2400 3fff
#m=8
#x=adr
#b= -73728
#y= m*x + b

    def createMatrix(self,mem):
        pixels=[]
        #obtain bits
        for i in mem:
            for bit in range(7,-1,-1):
                px=(i>>bit) & 0x01
                pixels.append(px)
        #create array of numpy
        mat = np.array(pixels)
        #resize array of numpy for screen
        mat = np.resize(mat,(256,224))
        #transpose mat for getting correct data
        self.matrix = mat.transpose()

    def normal(self):
        for i,row in enumerate(self.matrix):
            for j,col in enumerate(row):
                if col == 1:
                    self.Screen.set_at((i,j),self.WHITE)
                else:
                    self.Screen.set_at((i,j),self.BLACK)
        pygame.display.flip()
        

    def load(self,Mem):
        self.createMatrix(Mem.getScreenMemory())
        self.normal()

    def display(self,Mem):
        self.load(Mem)
    
    def resetScreen(self,Mem):
        self.load(Mem)

if __name__ == '__main__':

    s = Screen()
    m = Memory()
    #m.Load("invaders.rom")

    for i in range(0x2400,0x2500):
        m.setMemory(i,0xff)

    print(m.Memory[0x2400:0x2500])
    halt = False
    while not halt:
        s.display(m)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == 274:
                    pygame.quit()
                    halt = True