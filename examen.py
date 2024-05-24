class Engin:
    "machine destiné a une fonction"
    def __init__(self,nomengin,datefabrication,maisonfab,prix,etat):
        self.nomengin=nomengin
        self.datefabrication=datefabrication
        self.maisonfab=maisonfab
        self.prix=prix
        self.etat=etat
    def reparer():
        pass
    def changer():
        pass

maintenant=Engin('moto',123,'palos',900)
maintenant.prix=5
print(maintenant.prix)

