import numpy as np
import scipy.stats as st
from pprint import pprint
from scipy.stats import poisson, chi2, chi2_contingency

print("EXERCICE 1___________________________________________________________________________________")
# À l’aide de 100 antennes GPS, en des points différents du globe1, le nombre de satellites visibles a été
# compté :



# Données
satellites = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
observations = np.array([6, 15, 9, 25, 17, 10, 8, 7, 3])
n = np.sum(observations)

# QUESTION 2.1 : Moyenne et variance
moyenne = np.sum(satellites * observations) / n
variance = np.sum(observations * (satellites - moyenne)**2) / n

print("Moyenne :", moyenne)
print("Variance :", variance)


# QUESTION 2.2 : Loi de Poisson
lam = 4.47
x = np.arange(0, 17)

effectifs_theoriques = n * poisson.pmf(x, lam)

print("\nEffectifs théoriques :")
for i in range(len(x)):
    print(f"{i} satellites : {effectifs_theoriques[i]:.3f}")



# QUESTION 2.3 : Test du Khi-deux
# H0 : les données suivent une loi de Poisson(4.47)
# H1 : les données ne suivent pas cette loi
alpha = 0.05

# Regroupement des classes pour éviter
# les effectifs théoriques trop faibles.
# Classes : 0-1, 2, 3, 4, 5, 6, 7, 8 et plus

obs = np.array([
    6, 15, 9, 25, 17, 10, 8, 7 + 3
])

theo = np.array([
    np.sum(effectifs_theoriques[:2]),
    effectifs_theoriques[2],
    effectifs_theoriques[3],
    effectifs_theoriques[4],
    effectifs_theoriques[5],
    effectifs_theoriques[6],
    effectifs_theoriques[7],
    n * poisson.sf(7, lam)
])


# Statistique du Khi-deux
X2 = np.sum((obs - theo)**2 / theo)

# 8 classes après regroupement
ddl = len(obs) - 1  # 7
seuil = chi2.ppf(1 - alpha, ddl)
p_value = chi2.sf(X2, ddl)

print("\nKhi-deux calculé :", X2)
print("Khi-deux critique :", seuil)
print("p-value :", p_value)

if X2 > seuil:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

print("\nCONCLUSION : On ne rejette pas H0. Les données sont compatibles avec une loi de Poisson(4.47).")

print("\nEXERCICE 2___________________________________________________________________________________")


# Tableau : lignes = sexe, colonnes = réponses
obs = np.array([
    [3, 9, 18, 36, 29],  # Hommes
    [3, 3, 1, 14, 13]    # Femmes
])

alpha = 0.05

# Effectifs théoriques
total_lignes = np.sum(obs, axis=1)
print(f"Total lignes : {total_lignes}")
total_colonnes = np.sum(obs, axis=0)
print(f"Total colonnes : {total_colonnes}")
n = np.sum(obs)


theo = np.outer(total_lignes, total_colonnes) / n

print("Effectifs théoriques :")
print(np.round(theo, 2))

# Test du Khi-deux
X2 = np.sum((obs - theo)**2 / theo)

ddl = (obs.shape[0] - 1) * (obs.shape[1] - 1)
seuil = chi2.ppf(1 - alpha, ddl)
p_value = chi2.sf(X2, ddl)

print("X² =", X2)
print("Degrés de liberté =", ddl)
print("Seuil critique =", seuil)
print("p-value =", p_value)

if X2 > seuil:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")



