import pyxel

class pose_fleur:
    def __init__(self, x, y, fleur, fleurType):
        self.plant = fleur
        self.plantSelect = fleurType
        self.plantLife = [300,500,100,1500,250]
        self.x = x
        self.y = y
        self.draw()
    
    def draw(self):
        pyxel.rect(1,95,6,6,9)      # plante rouge
        pyxel.rect(7,95,6,6,10)     # plante orage
        pyxel.rect(13,95,6,6,11)    # plante bleu
        pyxel.rect(19,95,6,6,12)    # plante rose
        pyxel.rect(25,95,6,6,13)    # plante violette
        
        # Plante qui pousse
        for i in range(len(self.plant)):
            # Plante completement poussé  
            if self.plant[i][3] <= 0:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.plant[i][0]-4 <= self.x <= self.plant[i][0]+3 and self.plant[i][1]-6 <= self.y <= self.plant[i][1]+2:
                    print("On recolte")
                    self.plant.remove(self.plant[i]) # Supression de la plante
                    break
                pyxel.blt(self.plant[i][0]-3,self.plant[i][1]-6,0,0,8+16*self.plant[i][4],8,8,0)
            
            # Plante poussé à 2 tiers
            elif self.plant[i][3] < self.plantLife[self.plant[i][4]]/3:
                pyxel.blt(self.plant[i][0]-3,self.plant[i][1]-6,0,8,0+16*self.plant[i][4],8,8,0)
                self.plant[i][3] -= 1
            
            # Plante commence à poussé
            elif self.plant[i][3] < self.plantLife[self.plant[i][4]] - 50:
                pyxel.blt(self.plant[i][0]-3,self.plant[i][1]-6,0,0,0+16*self.plant[i][4],8,8,0)
                self.plant[i][3] -= 1
                
            # Plante sous forme de graine
            elif self.plant[i][3] <= self.plantLife[self.plant[i][4]]:
                pyxel.rect(self.plant[i][0],self.plant[i][1],2,2,self.plant[i][2])
                self.plant[i][3] -= 1
        
        
        if pyxel.btn(pyxel.KEY_S):        
            if self.contour(self.x,self.y) == True:
                print("On plante")
                
                # position x, position y, couleur, durée de vie, type de plante
                self.plant.append([self.x,self.y,8,self.plantLife[self.plantSelect],self.plantSelect]) 
            
        return self.plant
    
    def contour(self, x,y):
        if (pyxel.pget(x,y) + pyxel.pget(x+2,y) + pyxel.pget(x-2,y) + pyxel.pget(x,y+2) + pyxel.pget(x,y-2) + pyxel.pget(x+2,y+2) + pyxel.pget(x+2,y-2) + pyxel.pget(x-2,y+2) + pyxel.pget(x-2,y-2) + pyxel.pget(x+3,y+1) + pyxel.pget(x+3,y-1) + pyxel.pget(x-3,y+1) + pyxel.pget(x-3,y-1) + pyxel.pget(x+1,y+3) + pyxel.pget(x-1,y+3) + pyxel.pget(x+1,y-3) + pyxel.pget(x-1,y-3) + pyxel.pget(x+3,y+3) + pyxel.pget(x+3,y-3) + pyxel.pget(x-3,y+3) + pyxel.pget(x-3,y-3) ) / 21 == 4: 
            return True
        else:
            return False 