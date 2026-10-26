import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


print("EXERCICE 2 : PROMOTION HOMOGENE __________________________________________________")

# QUESTION 2.1 : comparaison des moyennes de deux populations
# H0 : les deux promotions ont la meme moyenne
# H1 : les deux promotions ont des moyennes differentes
# Les effectifs sont grands : approximation normale de la difference des moyennes.

n1, n2 = 90, 72
m1, m2 = 12.2, 13
s1, s2 = 4.2, 3.8
alpha = 0.05

z = (m1 - m2) / np.sqrt(s1**2 / n1 + s2**2 / n2)
seuil = st.norm.ppf(1 - alpha / 2)
p_value = 2 * st.norm.sf(abs(z))

print("H0 : moyennes egales ; H1 : moyennes differentes")
print("Statistique Z =", z)
print("Seuil critique = +/-", seuil)
print("p-value =", p_value)
if abs(z) > seuil:
    print("On rejette H0 : difference significative entre les moyennes.")
else:
    print("On ne rejette pas H0 : pas de difference significative entre les moyennes.")


print("\nEXERCICE 3 : BIEN DOSER L'ALLIAGE ______________________________________________")

# Donnees : resistance a la traction pour chaque proportion de carbone
acier_01 = np.array([23.05, 36, 31.1, 32.65, 30.9, 31.4, 30.85])
acier_02 = np.array([41.85, 25.65, 46.7, 34.5, 36.65, 31.45, 36.13])
acier_04 = np.array([47.05, 43.45, 43, 38.65, 41.85, 35.45, 41.57])
acier_06 = np.array([49.65, 73.9, 66.45, 74.55, 62.4, 63.75, 65.11])

donnees = np.array([acier_01, acier_02, acier_04, acier_06])
proportions = ["0.1 %", "0.2 %", "0.4 %", "0.6 %"]

# QUESTION 3.1 : nature des variables
print("\nQUESTION 3.1")
print("Proportion de carbone : facteur qualitatif (4 modalites pour ce test).")
print("Resistance a la traction : variable quantitative continue.")

# QUESTION 3.2 : moyennes, variances et boites a moustaches
print("\nQUESTION 3.2")
moyennes = np.mean(donnees, axis=1)
variances = np.var(donnees, axis=1)  # division par n : formule du sujet

for i in range(len(proportions)):
    print(proportions[i], ": moyenne =", moyennes[i], "; variance =", variances[i])

plt.boxplot(donnees.T, labels=proportions)
plt.xlabel("Proportion de carbone")
plt.ylabel("Resistance a la traction")
plt.title("Resistance a la traction selon la proportion de carbone")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

print("Commentaire : la resistance tend a augmenter avec la proportion de carbone,")
print("notamment pour le groupe a 0.6 %. La dispersion varie selon les groupes.")

# QUESTION 3.3 : test de Fisher (analyse de variance a un facteur)
# H0 : les quatre moyennes sont egales
# H1 : au moins une moyenne est differente
print("\nQUESTION 3.3")
alpha = 0.05
p = len(donnees)                 # nombre de classes : 4
n_i = len(donnees[0])           # 7 observations par classe
n = p * n_i                     # nombre total d'observations : 28
moyenne_globale = np.mean(donnees)

# Dispersion intra-classe : moyenne des variances ponderees par les effectifs
SW2 = np.sum(n_i * variances) / n

# Dispersion inter-classes : ecarts des moyennes a la moyenne globale
SB2 = np.sum(n_i * (moyennes - moyenne_globale)**2) / n

# Statistique et seuil de la loi de Fisher (formule donnee page 4 du TP)
f0 = (SB2 / (p - 1)) / (SW2 / (n - p))
ddl1 = p - 1
ddl2 = n - p
seuil = st.f.ppf(1 - alpha, ddl1, ddl2)
p_value = 1 - st.f.cdf(f0, ddl1, ddl2)

print("H0 : les 4 moyennes sont egales")
print("Moyenne globale =", moyenne_globale)
print("Dispersion intra-classe SW^2 =", SW2)
print("Dispersion inter-classes SB^2 =", SB2)
print("F calcule =", f0)
print("Degres de liberte =", ddl1, "et", ddl2)
print("Seuil critique =", seuil)
print("p-value =", p_value)

if f0 > seuil:
    print("On rejette H0 : la proportion de carbone influence la resistance a la traction.")
else:
    print("On ne rejette pas H0 : influence non mise en evidence au seuil de 5 %.")
