from django import forms
from django.forms import ModelForm
from management_App.models import *
class formArticle(ModelForm):
    categorie=forms.ModelMultipleChoiceField(queryset=Categorie.objects.all())
    class Meta:
        model=Article
        fields=['nom','prixAchat','prixVente','quantiteEntree','categorie','tauxTva',]
class CatForm(ModelForm):
    articles=forms.ModelMultipleChoiceField(queryset=Article.objects.all())
    class Meta:
        model=Categorie
        fields=['nom','articles']
class CommandForm(ModelForm):
    """" formulaire la table categorie"""
    nomArticle=forms.ModelMultipleChoiceField(queryset=Article.objects.all())
    destination=forms.ModelChoiceField(queryset=Destination.objects.all())
    class Meta:
        model=Command
        fields=['nomArticle','quantiteCom','destination','livraison','description']

class OutputForm(ModelForm):
    """"Formulaire des sorties """  
    label=forms.ModelMultipleChoiceField(queryset=Article.objects.all())
    destination=forms.ModelChoiceField(queryset=Destination.objects.all())
    class Meta:
        model=Output
        fields=['label','quantite','destination','description']
class InputForm(ModelForm):
    class Meta:
        model=Article
        fields=['nom','quantiteEntree']
class SpendForm(ModelForm):
    """formulaire de depenses"""
    acteur=forms.ModelChoiceField(queryset=Employee.objects.all())
    class Meta:
        model=Spending
        fields=['montant','acteur','devise','motif']
class AgentForm(ModelForm):
    class Meta:
        model=Employee
        fields=['nom','prenom','nomUtilisateur','passWord','tel']
class RechecheForm(ModelForm):
    class Meta:
        model=Article
        fields=['nom']