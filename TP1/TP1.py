# CIPRIANI VILLENEUVE

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

print(f"Species : {speciesname}")

save_hist_variants: bool = True
status : bool = True #Permet de skip les graphiques

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

# plt.savefig("graphique_2_2.png")
plt.show(block = status)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 2.3 Étude de la variable petalLength

# Question 2.7: Tracer l’histogramme et l’histogramme cumulé. Faire varier le nombre d’intervalles de l’histogramme.

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 7))


##########################################################################################
# intervalle = 10
intervalle = "auto"
n  = len(petallength)
intervalle_Sturge = int(np.ceil(1 + 3.3 * np.log10(n)))
intervalle_yule = int(np.ceil(2.5 * n**0.25))
print(f"Intervalle Sturge : {intervalle_Sturge}\nIntervalle Yule : {intervalle_yule}")
##########################################################################################


plt.title(f"Étude de la variable petalLength avec intervalle : {intervalle}")
# ax1.hist(petallength, bins=intervalle_Sturge, edgecolor='black')
ax1.hist(petallength, bins=intervalle, edgecolor='black')
ax1.set_title("Histogramme : petallength")
ax1.set_ylabel("longueur (mm)")
ax1.set_xlabel("Quantité (qty)")
# ax2.hist(petallength, bins=intervalle_Sturge,cumulative = True, edgecolor='black')
ax2.hist(petallength, bins=intervalle,cumulative = True, edgecolor='black')
ax2.set_title("Histogramme cumulatif : petallength")
ax2.set_ylabel("longueur (mm)")
ax2.set_xlabel("Quantité (qty)")



#########################################################################################################
#Dédié au rapport
if save_hist_variants:

    liste_intervalles = [5, 10, 15, 20]

    for nb_intervalles in liste_intervalles:

        fig_hist, ax_hist = plt.subplots(figsize=(8, 6))

        ax_hist.hist(
            petallength,
            bins=nb_intervalles,
            edgecolor="black"
        )

        ax_hist.set_title(
            f"Histogramme petalLength - {nb_intervalles} intervalles"
        )
        ax_hist.set_xlabel("Longueur des pétales")
        ax_hist.set_ylabel("Effectif")

        nom_fichier = f"histogramme_petallength_{nb_intervalles}_intervalles.png"

        fig_hist.savefig(nom_fichier, dpi=300, bbox_inches="tight")

        plt.close(fig_hist)
#########################################################################################################

# Question 2.8: Décrire les caractéristiques de l’histogramme et analyser ces caractéristiques en fonction du nombre d’intervalles.


# Question 2.9: Tracer la boîte à moustaches (boxplot) et rappeler les différents éléments la constituant.
ax3.boxplot(petallength)
ax3.set_title("Boïte à moustache : petallength")
name = "graphique_2_3_interv_"+ str(intervalle) +".png"
# plt.savefig("graphique_2_3_interv_.png")
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