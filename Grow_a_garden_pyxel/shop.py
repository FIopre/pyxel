import pyxel

class shop:
    def __init__(self):
        self.soil=True
    
    def Open(self):
        self.soil = not self.soil
        if self.soil == True:
            pyxel.camera(0,0)
        else:
            pyxel.camera(100,100)




