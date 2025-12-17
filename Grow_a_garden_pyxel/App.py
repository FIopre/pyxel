import pyxel
import shop
import stock
import fleurs

PLANT_COLOR = ["rouge", "orange", "bleu", "rose", "violette"]
PLANT_PRICE = [20,30,50,150,220]

class App: 
    def __init__(self):
        pyxel.init(101, 101, title="Grow a garden")
        pyxel.mouse(True)
        pyxel.load("res.pyxres")
        
        self.fleurs = []
        self.plantType = 0
        
        self.graine = stock.Stock() # Le stock de graine
        self.shop = shop.shop()
        
        self.graine.gagner_une_graine("rouge")
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_M):
            self.shop.Open()
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 85<=pyxel.mouse_x<=100 and 85<=pyxel.mouse_y<=100 and self.shop.soil == True :
            self.shop.Open()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit

            
        if pyxel.btnp(pyxel.KEY_A) and self.graine.argent >= PLANT_PRICE[self.plantType]:
            self.flower.loot -= PLANT_PRICE[self.plantType]
            self.graine.gagner_une_graine(PLANT_COLOR[self.plantType])
        
        
    
    def draw(self):
        pyxel.cls(11)
        pyxel.rectb(0, 0, 101, 101, 6)
        pyxel.rect(1,1,99,99,4)
        if self.shop.soil == True:
            pyxel.blt(85,85,0,0,16, 16,16,0)
        
        for fleur in self.fleurs:
            if(fleur.is_alive):
                fleur.update(pyxel.mouse_x, pyxel.mouse_y)
            else:
                self.graine.argent += fleur.fleurValeur
                self.fleurs.remove(fleur)
        
        if self.plantType == 0:
            pyxel.text(3,87,str(self.graine.graine["rouge"]),7)      # plante rouge
        elif self.plantType == 1:
            pyxel.text(10,87,str(self.graine.graine["orange"]),7)    # plante orage
        elif self.plantType == 2:
            pyxel.text(17,87,str(self.graine.graine["bleu"]),7)    # plante bleu
        elif self.plantType == 3:
            pyxel.text(24,87,str(self.graine.graine["rose"]),7)    # plante rose
        elif self.plantType == 4:
            pyxel.text(31,87,str(self.graine.graine["violette"]),7)# violette
       
        # Pose une fleur
        if pyxel.btn(pyxel.KEY_S) and self.graine.graine[PLANT_COLOR[self.plantType]] > 0:
            
            if(self.contour(pyxel.mouse_x, pyxel.mouse_y)):
                
                self.fleurs.append(fleurs.Fleur(pyxel.mouse_x, pyxel.mouse_y, self.plantType))
                self.graine.graine[PLANT_COLOR[self.plantType]] -= 1
                
        
        
        # Selection des fleurs
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 8:
                self.plantType = 0
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 9:
                self.plantType = 1
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 5:
                self.plantType = 2
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 14:
                self.plantType = 3
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 2:
                self.plantType = 4
            
        # Verifie le contour
    def contour(self, x, y):
        if (pyxel.pget(x,y) + pyxel.pget(x+2,y) + pyxel.pget(x-2,y) + pyxel.pget(x,y+2) + pyxel.pget(x,y-2) + pyxel.pget(x+2,y+2) + pyxel.pget(x+2,y-2) + pyxel.pget(x-2,y+2) + pyxel.pget(x-2,y-2) + pyxel.pget(x+3,y+1) + pyxel.pget(x+3,y-1) + pyxel.pget(x-3,y+1) + pyxel.pget(x-3,y-1) + pyxel.pget(x+1,y+3) + pyxel.pget(x-1,y+3) + pyxel.pget(x+1,y-3) + pyxel.pget(x-1,y-3) + pyxel.pget(x+3,y+3) + pyxel.pget(x+3,y-3) + pyxel.pget(x-3,y+3) + pyxel.pget(x-3,y-3) ) / 21 == 4:
            return True
        else:
            return False
        

App()