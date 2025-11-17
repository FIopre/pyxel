from tkinter import SE
import pyxel
import Pose_fleur
import Argent

class App:
    def __init__(self):
        pyxel.init(101, 101, title="Grow a garden")
        pyxel.mouse(True)
        pyxel.load("res.pyxres")
        self.fleur = []
        self.plantType = 0
        pyxel.run(self.update, self.draw)
    
    def update(self):
        Argent.argent()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
    
    def draw(self):
        pyxel.cls(1)
        pyxel.rectb(0, 0, 101, 101, 6)
        pyxel.rect(1,1,99,99,4)
        
        Pose_fleur.pose_fleur(pyxel.mouse_x, pyxel.mouse_y, self.fleur, self.plantType)
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 9:
                print("Plante rouge")
                self.plantType = 0
                
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 10:
                print("Plante orange")
                self.plantType = 1
                
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 11:
                print("Plante bleu")
                self.plantType = 2
                
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 12:
                print("Plante rouge")
                self.plantType = 3
                
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 13:
                print("Plante rouge")
                self.plantType = 4
            
            
        

App()
