# Question 2.1: Taper et comprendre les commandes Python suivantes:
from pprint import pprint
import matplotlib.pyplot as plt
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

# ///////////////////////////////////////////
# Question 2.1 : traçage d'un nuage de points
fig, (ax) = plt.subplots(figsize=(17, 7))
ax.scatter(petallength, petalwidth)
ax.set_title("Nuage de points : largeur vs longueur des pétales")
ax.set_ylabel("Petal length")
ax.set_xlabel("Petal width")


# Question 2.2: Rappeler la définition du coefficient de corrélation et le calculer par la fonction ((numpy.)corrcoef).

# le coefficient de correllation est le lien linéaire entre deux variables aléatoires

correlation_matrix = np.corrcoef(petallength, petalwidth)
print(correlation_matrix)

# matrice de sortie :
# [petallength x petallength   petallength x petalwidth
#  petalwidth x petallength    petalwidth x petalwidth]
# [[1.        0.9627571]
#  [0.9627571 1.       ]]

r = correlation_matrix[0][1]


def re_lin(x,y,r):

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    x_var = np.std(x)
    y_var = np.std(y)


    coef_dirr = r *(y_var/x_var)
    ord_orig = y_mean - (r*(y_var/x_var)*x_mean)

    lien_lineaire  = coef_dirr * x + ord_orig

    return lien_lineaire

regress_lin = re_lin(petallength,petalwidth,r)

ax.plot(petallength, regress_lin, 'b', label='regression_lineaire', color="red")

# Question 2.4: Analyser le lien entre les deux variables.
# C'est lié

# Question 2.5:

setosa = petallength[species == "Iris-setosa"]
versicolor = petallength[species == "Iris-versicolor"]
virginica = petallength[species == "Iris-virginica"]


fig2, ax2 = plt.subplots(figsize=(17, 7))
ax2.hist(setosa, bins="auto", alpha=0.6, edgecolor="gray", linestyle="--", label="Setosa")
ax2.hist(versicolor, bins="auto", alpha=0.6, edgecolor="gray", linestyle="--",label="Versicolor")
ax2.hist(virginica, bins="auto", alpha=0.6, edgecolor="gray", linestyle="--",label="Virginica")

# Question 2.6:
fig3, ax3 = plt.subplots(figsize=(17, 7))
ax3.boxplot(
    [setosa, versicolor, virginica],
    labels=["Setosa", "Versicolor", "Virginica"],
    vert=False,
    patch_artist=True,
    medianprops={"color": "black", "linewidth": 2},
    boxprops={"linewidth": 1.5,
              "facecolor": "white",},
    whiskerprops={"linewidth": 1.5},
    capprops={"linewidth": 1.5},
    flierprops={
        "marker": "o",
        "markersize": 5,
        "markerfacecolor": "gray",
        "markeredgecolor": "black"
    }
)
ax3.set_title("Longueur des pétales selon l'espèce")
ax3.set_xlabel("Longueur du pétale")
ax3.set_ylabel("Espèce")

ax3.grid(axis="x", linestyle="--", alpha=0.4)


ni = np.array([np.sum(species == type) for type in speciesname])
yi_mean = np.array([np.mean(petallength[species == name_specie]) for name_specie in speciesname])
y_mean = np.mean(petallength)
s_squared_Yi = np.array([np.var(petallength[species == name_specie]) for name_specie in speciesname])
# print(f"ni : {ni}\n yi : {yi_mean}\n y : {y_mean}")
n = np.sum(ni)

SB = (1 / n) * np.sum(ni * (yi_mean - y_mean) ** 2)
SW = (1 / n) * np.sum(ni * s_squared_Yi)

S_tot = SB + SW

rapport_correl = np.sqrt((SB/S_tot))

print(f"S2 : {SB}, S3 : {SW}, S_TOT : {S_tot} : rapport_correl : {rapport_correl}")

plt.show()