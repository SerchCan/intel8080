import pygame
import numpy as np
from Memoria import Memory
class Screen():
    def __init__(self):
        pygame.init()
        self.matrix=None
        self.size = self.width,self.height = 224,256
        self.BLACK = 0,0,0
        self.WHITE = 255,255,255
        self.b=True
        self.Screen = pygame.display.set_mode(self.size)
        self.Screen.fill(self.WHITE)
        pygame.display.update()

    def createMatrix(self,mem):
        pixels=[]
        #obtain bits
        for i in mem:
            for bit in range(8):
                px=(i>>bit) & 0x01
                pixels.append(px)
        
        #create array of numpy
        mat = np.array(pixels)
        #resize array of numpy for screen
        h, w = 256, 224
        mat = np.resize(mat,(w,h))
        mat = np.flipud(mat)
        self.matrix = mat
        

    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                addr = self.matrix[i][j]
                color = self.WHITE if addr else self.BLACK
                self.Screen.set_at((i,j),color)
            pygame.display.update()

            
    def createHMMatrix(self,Mem):
        scr=[]
        for i in range (0x4000-0x2400):
            for b in range(8):
                scr.append( (Mem[i] >> b) &0x01 )

        scr = np.array(scr)

        scr = np.resize(scr,(256,224))
        scr = np.fliplr(scr)
        scr = np.transpose(scr)
        self.matrix = scr


    def load(self,Mem):
        self.createHMMatrix(Mem.getScreenMemory())
        self.draw()
        #self.setScreen(Mem)

    def display(self,Mem):
        self.load(Mem)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 274:
                    pygame.quit()

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