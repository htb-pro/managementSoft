from django.urls import path
from management_App.views import *


urlpatterns = [
    path('List_article',article,name="articles"),
    path('detail/<articleId>',Detail,name="detail"),
    path('categorie',catArticle,name="categories"),
    path('entree',Entrees,name="entrees"),
    path('depence',Depences,name="depences"),
    path('agents',Agents,name="Agents"),
    path('distribution',Distribution,name="distribution"),
    path('sorties',Sorties,name="sorties"),
    path('stock',stocks,name="stocks"),
    path('commandes',Demandes,name="Commandes"),
    path('tableau',Dashboard,name="tableau"),
    path('EnregistrerArticle',FormulaireArticle,name="formulaireArticle"),
    path('suppression/<int:articleId>',Supprimer,name="supression"),
    path('Modification/<int:Idmodification>',Modifier,name="modification"),
    path('FormulaireCommande',FormCommand,name="formulaireCommande"),
    path('ModifierCommande/<int:comId>',ModifierCom,name="modificationCommande"),#modification de la commande
    path('suppressionCommande/<int:comId>',SupprimerCom,name="supressionCommande"),#suppression de la commande
    path('sortieForm',outputForm,name="formulaireSortie"),
    path('supressionSortie/<int:outId>',SupprimerSortie,name="suppressionsSortie"),
    path('modificationSortie/<int:outId>',ModifierSortie,name="modificationSortie"),
    path('FormulaireDepense',DepenseForm,name="formulaireDepense"),
    path('supressionDepense/<int:spendId>',SupprimerDepense,name="suppressionsDepense"),
    path('modificationDepense/<int:spendId>',ModifierDepense,name="modificationDepense"),
    path('formulaireCategorie',CategorieForm,name="formulaireCategorie"),
    path('formulaireAgent',FormAgent,name="formulaireAgents"),
    path('supressionAgent/<int:agentId>',SuprimerAgent,name="supressionAgent"),
    path('ModificationAgent/<int:agentId>',ModifierAgent,name="ModificationAgent"),
    path('ModificationEntree/<int:entreeId>',ModifierEntree,name="ModificationEntree"),
]
