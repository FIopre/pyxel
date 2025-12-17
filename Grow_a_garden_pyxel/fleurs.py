import pyxel

PLANT_LIFE = [300,500,900,1500,1950]
FLOWER_VALUE = [50,100,155,500,900]
PLANT_COLOR = ["rouge", "orange", "bleu", "rose", "violette"]

class Fleur:
    def __init__(self, x, y, fleurType):
        self.x = x
        self.y = y
        
        self.is_alive = True
        
        self.fleurType = fleurType
        self.fleurVie = PLANT_LIFE[fleurType]
        self.fleurValeur = FLOWER_VALUE[fleurType]
    
    def update(self, x, y):
        # Plante completement pousse 
        if self.fleurVie <= 0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x-4 <= x <= self.x+3 and self.y-6 <= y <= self.y+2:
                self.is_alive = False
            pyxel.blt(self.x-3,self.y-6,1,0,8+16*self.fleurType,8,8,0)
            
            # Plante pousse a 2 tiers
        elif self.fleurVie < PLANT_LIFE[self.fleurType]/3:
            pyxel.blt(self.x-3,self.y-6,1,8,0+16*self.fleurType,8,8,0)
            self.fleurVie -= 1
            
            # Plante commence a pousse 
        elif self.fleurVie < PLANT_LIFE[self.fleurType] - 50:
            pyxel.blt(self.x-3,self.y-6,1,0,0+16*self.fleurType,8,8,0)
            self.fleurVie -= 1
                
            # Plante sous forme de graine
        elif self.fleurVie <= PLANT_LIFE[self.fleurType]:
            pyxel.rect(self.x, self.y, 2, 2, 8)
            self.fleurVie -= 1