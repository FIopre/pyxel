import pyxel

class shop:
    def __init__(self):
        self.soil=True
        self.cam_x = 0
        self.cam_y = 0
    
    def Open(self):
        self.soil = not self.soil
        if self.soil == True:
            self.cam_x = 0
            self.cam_y = 0
        else:
            self.cam_x = 100
            self.cam_y = 100
        pyxel.camera(self.cam_x, self.cam_y)




