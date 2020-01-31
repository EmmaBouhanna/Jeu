class Monstre:
    def __init__(self):
        self.force = None
        self.vie = True
    
    def vaincu(self):
        self.vie = False


class Chevalier(Monstre):
    def __init__(self):
        super().__init__(self)
        self.force = 10
        

class Objet:
    def __init__(self): # le type de la pièce vient de la classe de sandra
        self.donne = 0
        


class Potion(Objet):
    def __init__(self):
        self.donne = 1 # point de vie
class Nourriture(Objet):
    def __init__(self):
        self.donne = 1 # point de force 

class Argent(Objet):
    def __init__(self):
        self.donne = random.randint(5, 11)


class Armure(Objet):
    def __init__(self):
        self.donne = random.randint(1,5)

class Arme(Objet):
    def __init__(self):
        self.donne = random.randint(4, 6) 



class Personnage:
    def __init__(self):
        self.force = 10
        self.pt_vie = 3
        self.defense = 10
        self.sac = []
        self.armes = []
        self.pos = [18, 40]
        self.tirelire = 0
          
        
    def move_me(self, grid, dx, dy):
        x = self.pos[0]+dx
        y = self.pos[1]+dy
        el = grid[x, y]
        if el == 2 or el == 3 or el == 4:
            self.pos[0], self.pos[1] = x, y
        if el == 11:
            potion = Potion()
            grid[x,y] = 4
            self.pt_vie += potion.donne
            self.pos[0], self.pos[1] = x, y
        if el == 12:
            nourriture = Nourriture()
            grid[x,y] = 4
            self.force += nourriture.donne
            self.pos[0], self.pos[1] = x, y
        if el == 13:
            argent = Argent()
            grid[x,y] = 4
            self.tirelire += argent.donne
            self.pos[0], self.pos[1] = x, y
        if el == 14:
            a = Armure()
            grid[x,y] = 4
            self.defense += armure.donne
            self.pos[0], self.pos[1] = x, y
        if el == 15:
            a = Arme()
            grid[x,y] = 4
            self.sac.append(a)
            self.force += arme.donne
            self.pos[0], self.pos[1] = x, y



