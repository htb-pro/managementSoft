from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
#pswadmin:Htb->12345
from django.db import models

class Categorie(models.Model):
    class Meta:
        verbose_name="Categorie"
        verbose_name_plural="Categories"
    nom=models.CharField(max_length=30, default="")
    articles=models.CharField(max_length=50)
    # Pour les articles d'une categorie on va les prendre via la relation 
    def __str__(self) -> str:
        return self.nom
class Article(models.Model):
    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
    nom=models.CharField(max_length=50, unique=True,verbose_name="Article")
    prixAchat=models.IntegerField(default=0,verbose_name="Prix d'achat")
    prixVente=models.IntegerField(default=0,verbose_name="Prix de vente")
    tauxTva=models.FloatField(default=0,null=True,verbose_name="Tva")
    date=models.DateField(auto_now_add=True)# la date d'enregistrement
    quantiteEntree=models.IntegerField(default=0,verbose_name="Quantite")
    categorie=models.ManyToManyField(Categorie,verbose_name="Categorie")
    def __str__(self) -> str:
        return self.nom

class Input(models.Model):
    class Meta:
        verbose_name="Input"
        verbose_name_plural="Inputs"
    label=models.ManyToManyField(Article)
    # en ce qui concerne la quantite d'entrer elle sera celle qui est dans la table article
    # la date egelement 
class Destination(models.Model):
    class Meta:
        verbose_name="Destination"
        verbose_name_plural="Destinations"
    nomDestination=models.CharField(max_length=25)
    def __str__(self) -> str:
        return self.nomDestination
class Output(models.Model):
    class Meta:
        verbose_name="Output"
        verbose_name_plural="Outputs"
    label=models.ManyToManyField(Article,verbose_name="Article")
    quantite=models.IntegerField(default=0)
    destination=models.ForeignKey(Destination,on_delete=models.CASCADE,verbose_name="Distribution")
    date=models.DateField(auto_now_add=True)
    description=models.TextField(blank=True)
class Stock(models.Model):
    """table de la sortie"""
    article=models.CharField(max_length=50,verbose_name="Articles")
    status=models.IntegerField(default=0,verbose_name="Etat")
    date=models.DateField(auto_now=True,verbose_name="Date")
    quantiteEntree=models.ManyToManyField(Article,verbose_name="Articles")
    quantiteSortie=models.ManyToManyField(Output,verbose_name="Sorties")
    """@property
    def sold(self):
        result=self.quantiteEntree.label.quantite 
        return result"""
   
#on doit prendre le nom de l'article par sortie avec _creat()
class Employee(models.Model):
    class Meta:
        verbose_name="Employee"
        verbose_name_plural="Employees"
    nom=models.CharField(max_length=20,verbose_name="Nom")
    prenom=models.CharField(max_length=20,verbose_name="Prenom")
    nomUtilisateur=models.CharField(max_length=20,verbose_name="Nom d'Utilisateur")
    passWord=models.CharField(max_length=10,verbose_name="Mot de passe")
    tel=models.CharField(max_length=13,unique=True,verbose_name="Numero")
    def __str__(self) -> str:
        return self.nom
class Command(models.Model):
    nomArticle=models.ManyToManyField(Article,verbose_name="Articles")
    quantiteCom=models.IntegerField(default=0)#quantite commandé
    destination=models.ForeignKey(Destination,on_delete=models.CASCADE,verbose_name="Distribution")
    dateCom=models.DateField(auto_now_add=True)#date de la commande
    description=models.TextField(blank=True)
    choix=[("Livré","Livre"),("Nonlivré","Non livre")]
    livraison=models.CharField(max_length=50,choices=choix)#ce champs doit etre une list de choix Livre ou non livre
    """on doit gerer les commandes cad savoir lequels sont livres et non livres"""
class Spending(models.Model):
    date=models.DateField(auto_now_add=True)
    montant=models.FloatField(default=0)
    devises=[("fr","FC"),("usd","USD")]
    devise=models.CharField(max_length=50,choices=devises,verbose_name="Devise")
    acteur=models.ForeignKey(Employee,on_delete=models.CASCADE,verbose_name="Agent")
    motif=models.TextField(verbose_name="Raison")
    """def __str__(self) -> str:
        return self.motif """#la personne qui a effectuer la depense



# Create your models here.

