
# Question 2.1: Taper et comprendre les commandes Python suivantes:
from pprint import pprint
import numpy as np
# Lire le fichier CSV avec numpy (assume un header)
data = np.genfromtxt("iris.csv", delimiter=",",
names=True, dtype=None, encoding="utf-8")
# Colonnes
sepallength = data["sepallength"]
sepalwidth = data["sepalwidth"]
petallength = data["petallength"]
petalwidth = data["petalwidth"]
species = data["class"]
speciesname = np.unique(species)

status : bool = False #Permet de skip les graphiques

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 2.1 Analyse préalable

# Question 2.2: Quel est le nombre d’individus statistiques?
nb_individu : int  = len(data)
print(f"nombre d’individus statistiques : {nb_individu}")

# Question 2.3: Trouver les variables qualitatives et leurs valeurs possibles. Sont-elles nominales ou ordinales ?

# Il existe une seule variable quantitative qui est "class" qui définir le type d'iris 
# Ici l'ordre ne compte pas donc nominales,

# Question 2.4: Trouver les variables quantitatives. Sont-elles continues ou discrètes?
# Dans le cas présent, le excell présente les infos suivantes : "sepallength","sepalwidth","petallength","petalwidth" -> elles sont continues car en type float
# print(data.dtype.names)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 2.2 Étude de la variable species

# Question 2.5: Quels sont les effectifs de chaque valeur de cette variable ?
dico_data_effectives = dict()
for type in speciesname:
    # dico_data_effectives[type] = {}
    dico_data_effectives[type]= np.sum(species == type)

pprint(dico_data_effectives, indent=4, width=80)


# Question 2.6
import matplotlib.pyplot as plt

labels = dico_data_effectives.keys()
sizes = dico_data_effectives.values()
print(sizes)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.pie(sizes, labels=labels)

ax2.hist(species, bins=3, edgecolor='black',label=labels)

plt.savefig("graphique_2_2.png")
plt.show(block = status)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 2.3 Étude de la variable petalLength

# Question 2.7: Tracer l’histogramme et l’histogramme cumulé. Faire varier le nombre d’intervalles de l’histogramme.

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 7))
intervalle = "auto"
intervalle = 5


plt.title(f"Étude de la variable petalLength avec intervalle : {intervalle}")

ax1.hist(petallength, bins=intervalle, edgecolor='black')
ax1.set_title("Histogramme : petallength")
ax1.set_ylabel("longueur (mm)")
ax1.set_xlabel("Quantité (qty)")

ax2.hist(petallength, bins=intervalle,cumulative = True, edgecolor='black')
ax2.set_title("Histogramme cumulatif : petallength")
ax2.set_ylabel("longueur (mm)")
ax2.set_xlabel("Quantité (qty)")



# Question 2.8: Décrire les caractéristiques de l’histogramme et analyser ces caractéristiques en fonction du nombre d’intervalles.


# Question 2.9: Tracer la boîte à moustaches (boxplot) et rappeler les différents éléments la constituant.
ax3.boxplot(petallength)
ax3.set_title("Boïte à moustache : petallength")
name = "graphique_2_3_interv_"+ str(intervalle) +".png"
plt.savefig("graphique_2_3_interv_.png")
plt.show(block = status)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Deuxième approche : résumés numériques
# Question 2.10
mean_petallength = np.mean(petallength)
median_petallength = np.median(petallength)
print(f"Mean : {mean_petallength}\nMedian : {median_petallength}")

ecartType_petallength = np.std(petallength)
variance_petallength = np.var(petallength)
quartile_petallength = np.quantile(petallength, q=[0.25, 0.75])
print(f"Ecart_type : {ecartType_petallength}\nVariance : {variance_petallength}\nQuartile : {quartile_petallength}")

# Mean : 3.758666666666666
# Median : 4.35
# Ecart_type : 1.7585291834055212
# Variance : 3.092424888888889
# Quartile : [1.6 5.1]

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////