from abc import ABC
class Moteur(ABC):
    def qualiter(self):
        print('ce monteur est conçu aux etas unis')
        #encapsulqtion

class Engin(Moteur):
    "machine destiné a une fonction"
    def __init__(self,nomengin,datefabrication,maisonfab,prix,etat):
        self.__nomengin=nomengin
        self.__datefabrication=datefabrication
        self.__maisonfab=maisonfab
        self.__prix=prix
        self.__etat=etat
    def reparer(self,message="reparation engin gratuit pour delai de 2 mois"):
        print(message)
    def changer(self):
        print("changer l'engin si toutes les fonctionnalités ne s'execute pas")
        
class Voiture(Engin):
    # notion sur la surcharge
    def reparer(self):
        super().reparer(message="cette voiture ne peut pas etre reparee")

b=Voiture(2,3,4,2,5)
print(b.reparer())
print(b.qualiter())

