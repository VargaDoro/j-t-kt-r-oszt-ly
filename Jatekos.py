import random

class Jatekos:
    def __init__(self, nev:str="Játékos", poz:int="0", kaszt:str="harcos", emo:str="H"):
        self.nev=nev
        self.poz=poz
        self.kaszt=kaszt
        self.emo=emo
        self.hp=3+random.randint(1,6)

    """pozicíó beállítása tagfüggvény set_pozicio - setter"""
    def set_pozicio(self):
        self.poz=random.randint(0,2) #0-tól 2-2 lévő mezőkőn ugrálhatnak

    def set_hp(self):
        self.hp=self.hp-random.randint(0,1)# random fog csökkeni vagy 1-et vagy 0-át a hp 

    def __str__(self):
        return f"Név: {self.nev}, Pozíció: {self.poz}, Kaszt: {self.kaszt}, Életerő: {self.hp}, Karakter: {self.emo}"
    