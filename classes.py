class Monstre:
    def __init__(self,force,vie=True):
        self.force
    
    def deplacement()
    def vaincu
        self.vie
        self.donne_force
        self.donne_vie
    def avaincu
        self.dommages=


class Chevalier(Monstre):
    

class Objet:
    def __init__(self, piece): # le type de la pièce vient de la classe de sandra
        self.donne = 0
        self.localisation = (random.randint(len(piece.largeur), random.randint(len(piece.longueur)))


class Potion(Objet):
    def __init__(self, piece):
        self.donne = 1 # point de vie
        self.localisation = Objet.localisation
class Nourriture(Objet):
    def __init__(self,piece):
        self.donne = 1 # point de force 
        self.localisation = Objet.localisation

class Argent(Objet):
    def __init__(self):
        self.donne = random.randint(5, 11)
        self.localisation = Objet.localisation


class Armure(Objet):
    def __init__(self, piece):
        self.donne = random.randint(1,5)
        self.localisation = Objet.localisation

class Arme(Objet):
    def __init(self, piece)
        self.localisation = Objet.localisation
        self.donne = random.randint(4, 6) 



class Personnage:
    def __init__(self):
        self.force = 10
        self.pt_vie = 3
        self.sac = []
        self.armes = []
        self.pos = [] 
    
    def __repr__(self):
        print("@")
    
    def attack(self):
          
        
    def move_me(self, dx, dy):
        x = self.pos[0]+dx
        y = self.pos[1]+dy
        el = grid.get_el(x*grid.cell_size, (y)*grid.cell_size)
        
        if el == "." or el == "+" or el == "#":
            self.pos[0] = x
            self.pos[1] = y 
            return True
        # if el == "B" or el == "K":
            
        else:
            return False


