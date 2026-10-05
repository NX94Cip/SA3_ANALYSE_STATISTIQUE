import numpy as np
import scipy.stats as st

print("\n")
#Exercice 1 ________________________________________________________________________________
print("EXERCICE 1___________________________________________________________________________________")
# Paramètre d'intérêt : proportion p
# H0 : p = 0.20
# H1 : p < 0.20  -> test unilatéral inférieur

n = 100
p_0 = 0.20
p_hat = 0.15
alpha = 0.05

print(f"n = {n} > 30 : {n > 30}")
print(f"n*p_0 = {n*p_0} > 5 : {n*p_0 > 5}")
print(f"n*(1-p_0) = {n*(1-p_0)} > 5 : {n*(1-p_0) > 5}")

z_0 = (p_hat - p_0) / np.sqrt(p_0 * (1 - p_0) / n)
print(f"z_0 = {z_0}")

z_alpha = st.norm.ppf(alpha)
print(f"z_alpha = {z_alpha}")

#Verif Z_alpha
if z_0 < z_alpha:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

#Verif p-valeur
p_valeur = st.norm.cdf(z_0)
print(f"p-valeur = {p_valeur}")

if p_valeur < 0.05:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

print("CONCLUSION : On ne rejette pas H0. Les données ne permettent pas de conclure que la proportion est significativement inférieure à 20%.")
print("\n")

#Exercice 2 ________________________________________________________________________________
print("EXERCICE 2___________________________________________________________________________________")
# Paramètre d'intérêt : moyenne m
# H0 :µ = µ_0 = 37.5
# H1 :µ != µ_0

mu_0 = 37.5

T16 = [39, 39, 40, 33, 36, 40, 37, 41, 39, 34,
       42, 41, 42, 44, 42, 42, 39, 42, 41, 40,
       43, 43, 40, 39, 37]

n = len(T16)
if n < 30:
    print(f"n = {n} < 30 : {n < 30} : On utilise la loi de Student")
else:
    print(f"n = {n} > 30 : {n > 30} : On utilise la loi normale")

t_0 = (np.mean(T16) - mu_0) / (np.std(T16, ddof=1) / np.sqrt(n))
t_alpha_2 = st.t.ppf(1 - 0.05/2, df=n-1)
print(f"t_0 = {t_0}")
print(f"t_alpha_2 = {t_alpha_2}")

if abs(t_0) > t_alpha_2:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

p_valeur = 2 * (1 - st.t.cdf(abs(t_0), df=n-1))
print(f"p-valeur = {p_valeur}")

if p_valeur < 0.05:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

print("CONCLUSION : On rejette H0. La température moyenne de 2016 est significativement différente de 37.5°C. L'année 2016 peut donc être considérée comme exceptionnelle.")
print("\n")

print("EXERCICE 3___________________________________________________________________________________")

# Paramètre d'intérêt : moyenne m
# H0 :µ = µ_0 = 0.8
# H1 :µ != µ_0


mu_0 = 0.8
m = 0.797
n = 100
ecart_type = 0.8/100 

if n < 30:
    print(f"n = {n} < 30 : {n < 30} : On utilise la loi de Student")
else:
    print(f"n = {n} > 30 : {n > 30} : On utilise la loi normale")

z_0 = (m - mu_0) / (ecart_type / np.sqrt(n))
z_alpha_2 = st.norm.ppf(1 - 0.05/2)
print(f"z_0 = {z_0}")
print(f"z_alpha_2 = {z_alpha_2}")

if abs(z_0) > z_alpha_2 or z_0 < -z_alpha_2:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

p_valeur = 2 * (1 - st.norm.cdf(abs(z_0)))
print(f"p-valeur = {p_valeur}")

if p_valeur < 0.05:
    print("On rejette H0")
else:   
    print("On ne rejette pas H0")

print("CONCLUSION : On rejette H0.")
print("Les données présentent suffisamment de preuves pour infirmer")
print("l'affirmation de l'entreprise selon laquelle la moyenne est de 80%.")


