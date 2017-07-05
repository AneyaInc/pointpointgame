########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 26/06/2017
# Module           : Intelligence Articielle
# Nom              : Iris
#
########################################################

from random import randrange
import time

from Environnement.pivot import Pivot

pivot = Pivot()

class IrisIA(object):

    ownDico = {}
    otherDico = {}
    score = 0
    attackDico = {}
    defenseDico = {}

    def __init__(self,color):
        self.color = color

    def buildDico(self,dico,point_dico,space,attack):
        #Parcourt le dictionnaire
        for k in dico:
            #Exploder le K par les enderscorts
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])

            top_left = pivot.get_point_top_left(x,y,space,point_dico)
            top_right = pivot.get_point_top_right(x,y,space,point_dico)


            self.makeBatlleDico(top_left,attack)
            self.makeBatlleDico(top_right,attack)

    def makeBatlleDico(self,dico,attack):
        if(len(dico)):
            point = str(str(dico['x'])+'_'+str(dico['y']))
            if(attack):
                if point in self.attackDico:
                    self.attackDico[point] = self.attackDico[point] + 1
                else:
                    self.attackDico[point] = 1
            else:
                if point in self.defenseDico:
                    self.defenseDico[point] = self.defenseDico[point] + 1
                else:
                    self.defenseDico[point] = 1


    def checkOwnDico(self,dico,space):
        if(len(self.attackDico) == 0):
            self.buildDico(self.ownDico,dico,space,True)
        return self.attackDico

    def checkOtherDico(self,dico,space):
        if(len(self.defenseDico) == 0):
            self.buildDico(self.otherDico,dico,space,False)
        return self.defenseDico

    def canBuild(self):
        pass

    def randPoint(self,can,point_dico):

        r = 5
        boucle = True

        while boucle:

            y = randrange(30, (540 - 30))
            yMod = y % 30
            x = randrange(30, (630 - 30))
            xMod = x % 30

            point = str(str(x)+'_'+str(y))

            if (yMod) | (xMod):
                boucle = True
            else:
                if point in point_dico:
                    boucle = True
                else:
                    boucle = False

        can.create_oval(x-r, y-r, x+r, y+r, fill=self.getColor())

        point = {}
        point['x'] = x
        point['y'] = y

        return point

    #Dictionnaire de point de l'IA. ce Dictionnaire permettra de connaitre tous les emplacements des points de l'IA.
    def getOwnDico(self):
        return self.ownDico

    #Modification du dictionnaire de l'IA
    def setOwnDico(self,coord):
        self.ownDico[coord] = self.getColor()

    #Dictionnaire de point du joueur. ce Dictionnaire permettra de connaitre tous les emplacements des points du joueur.
    def getOtherDico(self):
        return self.otherDico

    #Modification du dictionnaire du joueur
    def setOtherDico(self,coord,color):
        self.otherDico[coord] = color

    #Score de l'IA
    def getScore(self):
        return self.score

    #Modification du score de l'IA
    def setScore(self):
        return self.score + 1

    def getColor(self):
        return self.color
