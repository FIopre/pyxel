import pyxel

class hud:
    def update(self, argent, cam_x, cam_y):
        pyxel.cls(11)
        pyxel.rectb(0, 0, 101, 101, 6)
        pyxel.rect(1,1,99,99,4)

        # Cadre pour les couleurs
        pyxel.rect(0,93,8,8,0)
        pyxel.rect(7,93,8,8,0)
        pyxel.rect(14,93,8,8,0)
        pyxel.rect(21,93,8,8,0)
        pyxel.rect(28,93,8,8,0)
        
        # Carre de couleur
        pyxel.rect(1,94,6,6,8)      # plante rouge
        pyxel.rect(8,94,6,6,9)     # plante orage
        pyxel.rect(15,94,6,6,5)    # plante bleu
        pyxel.rect(22,94,6,6,14)    # plante rose
        pyxel.rect(29,94,6,6,2)    # plante violette
        
        # Ecris l'argent
        pyxel.text(1,1,str(argent),1)

        # Place le bouton du shop
        pyxel.blt(cam_x + 85, cam_y + 85,0,0,16, 16,16,0) 




