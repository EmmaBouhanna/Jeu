class Monstre:
    def __init__(self,force,vie=True):
        self.force
    
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
        self.defense = 10
        self.sac = []
        self.armes = []
        self.pos = [2, 3]
        self.tirelire = 0
          
        
    def move_me(self, grid, dx, dy):
        x = self.pos[0]+dx
        y = self.pos[1]+dy
        el = grid[x, y]
        if ((el == 0) or (el == 2) or (el == 3)):
            self.pos[0], self.pos[1] = x, y
        if el == "P":
            potion = Potion()
            self.vie += potion.donne
            self.pos[0], self.pos[1] = x, y
        if el == "N":
            nourriture = Nourriture()
            self.force += nourriture.donne
            self.pos[0], self.pos[1] = x, y
        if el == "O":
            argent = Argent()
            self.tirelire += argent.donne
            self.pos[0], self.pos[1] = x, y
        if el == "Armure":
            a = Armure()
            self.defense += armure.donne
            self.pos[0], self.pos[1] = x, y
        if el == "Arme":
            a = Arme()
            self.sac.append(a)
            self.force += arme.donne
            self.pos[0], self.pos[1] = x, y



