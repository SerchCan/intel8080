from Memoria import Memory


class Puertos(Memory):
    def __init__(self, TAMMEM=256):
        super().__init__(TAMMEM)

    def setPort(self, pos, device):
        self.setMemory(pos, device)

    def getPort(self, pos):
        return self.getMemory(pos)


if __name__ == "__main__":
    port = Puertos()
