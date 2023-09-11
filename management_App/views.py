from django.shortcuts import render,redirect
from management_App.models import *
from management_App.forms import *
from django.db.models import Sum
# Create your views here.
def index(request):
    
    return render(request,'app_files/index.html',context={})
def article(request):
    article=Article.objects.all()
    return render(request,'app_files/article.html',context={'articles':article})
def Detail(request,articleId):
    article=Article.objects.get(id=articleId)
    return render(request,'app_files/detailArticle.html',context={'articles':article})
def catArticle(request):
    categorie=Categorie.objects.all()
    return render(request,'app_files/categorie.html',context={'categories':categorie})
def Entrees(request):
    entrees=Article.objects.all()
    return render(request,'app_files/entree.html',context={'entrees':entrees})#a revoir pour que le programme agisse selon les attante
def Sorties(request):
    sortie=Output.objects.all()
    return render(request,'app_files/sorties.html',context={'sorties':sortie})
def Depences(request):
    depence=Spending.objects.all()
    return render(request,'app_files/depense.html',context={'depences':depence})
def Agents(request):
    agent=Employee.objects.all()
    return render(request,'app_files/employes.html',context={'agents':agent})
def Distribution(request):
    distribution=Destination.objects.all()
    return render(request,'app_files/Destination.html',context={'distributions':distribution})

def stocks(request):
    stock=Article.objects.all()
    output=Output.objects.all()
  

    return render(request,'app_files/stock.html',context={'stocks':stock,'quantiteSorties':output})
def Demandes(request):
    commande=Command.objects.all()
    return render(request,'app_files/commande.html',context={'commandes':commande})
def Dashboard(request):
    articles=Article.objects.all()
    totalEntree=Article.objects.aggregate(Quantite_Entree=Sum('quantiteEntree'))
    totalSortie=Output.objects.aggregate(Quantite_Sortie=Sum('quantite'))
    totalCommandeLivre=Command.objects.filter(livraison="Livré").aggregate(QuantiteLivre=Sum('quantiteCom'))
    totalComNonLivre=Command.objects.filter(livraison="Nonlivré").aggregate(Quantite=Sum('quantiteCom'))
    context={'articles':articles,'totalEntree':totalEntree,'totalSortie':totalSortie,'totalCommandeLivre':totalCommandeLivre,'totalComNonLivre':totalComNonLivre}
    return render(request,'app_files/Dashboard.html',context,)
#---------------------------------------------------- les urls ou formulaire d'enregistrement ou creation---------
def FormulaireArticle(request):
    if request.method=="POST":
        FormArt=formArticle(request.POST)
        if FormArt.is_valid():
            FormArt.save()
            return redirect('formulaireArticle')
    else:
        FormArt=formArticle()
    return render(request,'formulaires/FormArticle.html',context={'form':FormArt})
def Supprimer(request,articleId):
    article=Article.objects.get(id=articleId)
    article.delete()
    return redirect('articles')
def Modifier(request,Idmodification):
    artId=Article.objects.get(id=Idmodification)
    if request.method=="POST":
        FormArt=formArticle(request.POST,instance=artId)
        if FormArt.is_valid():
            FormArt.save()
            return redirect('articles')
    else:
        FormArt=formArticle(instance=artId)
    return render(request,'formulaires/FormArticle.html',context={'form':FormArt})
#----------------------------------------- la vie du formulaire de la categorie-----------------
def CategorieForm(request):
    if request.method=="POST":
        formCat=CatForm(request.POST)
        if formCat.is_valid():
            formCat.save()
            return redirect('formulaireCategorie')
    else:
        formCat=CatForm()
    context={'formulaireCat':formCat}
    return render(request,'formulaires/CategorieForm.html',context)
#-----------------------------------------Vue de la commande -----------------------------------------
def FormCommand(request):
    if request.method =="POST":
        ComForm=CommandForm(request.POST)
        if ComForm.is_valid():
            ComForm.save()
            return redirect('formulaireCommande')
    else:
        ComForm=CommandForm()
    context={'formCom':CommandForm}
    return render(request,'formulaires/CommandeForm.html',context)
def SupprimerCom(request,comId):
    """la vue de la supression d'une commande"""
    commande=Command.objects.get(id=comId)
    commande.delete()
    return redirect('Commandes')
def ModifierCom(request,comId):
    """la vue pour la modification de la commande"""
    CommandeId=Command.objects.get(id=comId)
    if request.method =="POST":
        ComForm=CommandForm(request.POST, instance=CommandeId) # on affiche les formulaire deja rempli
        if ComForm.is_valid():
            ComForm.save()
            return redirect('Commandes')# et on redirige vert la base de donnees des commandes 
    else:
        ComForm=CommandForm(instance=CommandeId)
    context={'formCom':CommandForm}
    return render(request,'formulaires/CommandeForm.html',context)
#--------------------------------------------------vue des sorties -----------------------------------
def outputForm(request):
    """"formulaire des aorties"""
    if request.method=="POST":
        OutForm=OutputForm(request.POST)
        if OutForm.is_valid():
            OutForm.save()
            return redirect ('formulaireSortie')
    else:
        OutForm=OutputForm()
    context={'formSortie':OutForm}
    return render(request,'formulaires/outputForm.html',context)

def SupprimerSortie(request,outId):
    """la vue de la suppressions des sorties"""
    outputId=Output.objects.get(id=outId)
    outputId.delete()
    return redirect("sorties")

def ModifierSortie(request,outId):
    """formulaire de modification"""
    outputId=Output.objects.get(id=outId)
    if request.method=="POST":
        OutForm=OutputForm(request.POST,instance=outputId)
        if OutForm.is_valid():
            OutForm.save()
            return redirect ('sorties')
    else:
        OutForm=OutputForm(instance=outputId)
    context={'formSortie':OutForm}
    return render(request,'formulaires/outputForm.html',context)

#-----------------------------------------vue de la depense -----------------------------------------
def DepenseForm(request):
    """la vue de la depense"""
    if request.method =="POST":     
        formDepense=SpendForm(request.POST)
        if formDepense.is_valid():
            formDepense.save()
            return redirect('formulaireDepense')
    else:
        formDepense=SpendForm()
    context={'formDepense':formDepense}
    return render(request,'formulaires/depenseForm.html',context)

def SupprimerDepense(request,spendId):
    """la vue de la suppressions des depense"""
    outputId=Spending.objects.get(id=spendId)
    outputId.delete()
    return redirect("depences")


def ModifierDepense(request,spendId):
    """formulaire de modification"""
    spendingId=Spending.objects.get(id=spendId)
    if request.method=="POST":
        formDepense=SpendForm(request.POST,instance=spendingId)
        if formDepense.is_valid():
            formDepense.save()
            return redirect ('depences')
    else:
        formDepense=SpendForm(instance=spendingId)
    context={'formDepense':formDepense}
    return render(request,'formulaires/depenseForm.html',context)
#----------------------------------------------------la vue du formulaire d'agents----------------------
def FormAgent(request):
    if request.method=="POST":
        formulaireAgent=AgentForm(request.POST)
        if formulaireAgent.is_valid():
            formulaireAgent.save()
            return redirect('formulaireAgents')
    else:
        formulaireAgent=AgentForm()
    context={'formulaireAgent':formulaireAgent}
    return render(request,'formulaires/FormulaireAgent.html',context)
def SuprimerAgent(request,agentId):
    """la vue de la suppression d'un agent"""
    AgentSuprime=Employee.objects.get(id=agentId)
    AgentSuprime.delete()
    return redirect('Agents')

def ModifierAgent(request,agentId):
    """la vue pour la modification des agents"""
    agentModifie=Employee.objects.get(id=agentId)
    if request.method=="POST":
        formulaireAgent=AgentForm(request.POST,instance=agentModifie)
        if formulaireAgent.is_valid():
            formulaireAgent.save()
            return redirect('Agents')
    else:
        formulaireAgent=AgentForm(instance=agentModifie)
    context={'formulaireAgent':formulaireAgent}
    return render(request,'formulaires/FormulaireAgent.html',context)

#-------------------------------------------------------
def ModifierEntree(request,entreeId):
    """modification d'une entree d'articles"""
    entreeApdateId=Article.objects.get(id=entreeId)
    if request.method=="POST":
        FormArt=InputForm(request.POST,instance=entreeApdateId)
        if FormArt.is_valid():
            FormArt.save()
            return redirect('entrees')
    else:
        FormArt=InputForm(instance=entreeApdateId)
    return render(request,'formulaires/FormArticle.html',context={'form':FormArt})
"""def formRecheche(request):
    if request.methode=="GET":
        Recherche=Article.objects.filter(nom=name)
        return redirect('articles')
    else:
        R"""