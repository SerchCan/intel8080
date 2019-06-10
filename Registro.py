class Registro:
    def __init__(self, value=0x00):
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


if __name__ == "__main__":
    r = Registro()
    r.setValue(5)
    print(r.getValue())
