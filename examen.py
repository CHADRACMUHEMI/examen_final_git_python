class Engin:
    "machine destiné a une fonction"
    def __init__(self,nomengin,datefabrication,maisonfab,prix,etat):
        self.nomengin=nomengin
        self.datefabrication=datefabrication
        self.maisonfab=maisonfab
        self.prix=prix
        self.etat=etat
    def reparer():
        print("reparation engin gratuit pour delai de 2 mois")
    def changer():
        print("changer l'engin si toutes les fonctionnalités ne s'execute pas")
class Voiture(Engin):
    def __init__(self,nomengin,datefabrication,maisonfab,prix,etat,marque):
        self.nomengin=nomengin
        self.datefabrication=datefabrication
        self.maisonfab=maisonfab
        self.prix=prix
        self.etat=etat
        self.marque=marque

maintenant=Engin('moto',123,'palos',900,'expire 4')
maintenant.prix=5
print(maintenant.prix)
vr=Voiture('moto',123,'palos',900,'expire 4','toyota')
print(vr.marque)

