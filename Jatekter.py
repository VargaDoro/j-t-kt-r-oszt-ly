from Jatekos import Jatekos
class Jatekter:
    def __init__(self):
#Pédányosítás
        self.harcos=Jatekos("Tubamtolog",0,"támogató","🦸‍♂️") #Emoji----> Billentyűzeten: windows + pont 
        self.varazslo=Jatekos("Waar'Ash Low",2,"varázsló","🧙‍♂️")
        self.lista=["_","_","_"]
        self.lista[self.harcos.poz]=self.harcos.emo
        self.lista[self.varazslo.poz]=self.varazslo.emo
        self.n=1
        self.kiir()

    def kiir(self):
        print(f"{self.n}.kör")
        print(f"*"*15,"     ","-"*27,"      ","-"*29,"      ")
        print(f"*   {self.lista[0]:<3} {self.lista[1]} {self.lista[2]:>3}    *     | A {self.harcos.nev} életereje: {self.harcos.hp} |   | A {self.varazslo.nev} életereje: {self.varazslo.hp}")
        print(f"*"*15,"     ","-"*27,"      ","-"*29,"      ")
        print("")

        """print(harcos)
        print(varazslo)"""

        """
        Játék
        dobunk kockával, az új poziciót, - ez a Játékos osztály feladat
        """
    def jatekmenet(self):
            
            while(self.harcos.hp>0 and self.varazslo.hp>0):
                self.harcos.set_pozicio() #lép a harcos
                self.varazslo.set_pozicio() #lép a varaazslo
                self.lista=["_","_","_"]
                self.lista[self.harcos.poz]=self.harcos.emo
                self.lista[self.varazslo.poz]=self.varazslo.emo
                if(self.harcos.poz==self.varazslo.poz):
                    self.lista[self.varazslo.poz]="💪"
                    """itt harcolnak"""
                    self.harcos.set_hp()
                    self.varazslo.set_hp()
                self.n+=1
                self.kiir()
                input()