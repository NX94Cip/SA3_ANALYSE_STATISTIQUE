import numpy as np
import scipy.stats as st

def interv_conf_inf_30(data, alpha):
    #Intervalle de confiance
    n = len(data)
    x_mean = np.mean(data)
    Ecart_type = np.std(data, ddof=1)
    fnct_repart_inv = st.t.ppf(1 - alpha/2, df=n-1)

    Int_CONF = np.array([x_mean - fnct_repart_inv*(Ecart_type/np.sqrt(n)),
                        x_mean + fnct_repart_inv*(Ecart_type/np.sqrt(n)) ])
    return Int_CONF


def interv_conf_grand_nombres(data, alpha):
    #Intervalle de confiance
    n = len(data)
    x_mean = np.mean(data)
    Ecart_type = np.std(data)
    Z_alpha_2 = st.norm.ppf(1 - alpha/2)

    Int_CONF = np.array([x_mean - Z_alpha_2*(Ecart_type/np.sqrt(n)),
                        x_mean + Z_alpha_2*(Ecart_type/np.sqrt(n)) ])
    return Int_CONF

def interv_conf_prop_grand_echantillon(data, component, percent, n):
    alpha = 1-percent
    prop_data = np.sum(data == component) / n
    Z_alpha_2 = st.norm.ppf(1 - alpha/2)
    I_C = np.array([prop_data - Z_alpha_2 * np.sqrt((prop_data * (1 - prop_data))/n),
                    prop_data + Z_alpha_2 * np.sqrt((prop_data * (1 - prop_data))/n)])
    return I_C

if __name__ == "__main__":

    print("/////////////////////////////////////////////")
    print("PARTIE 2")
    print("Question 2.1")
    data = np.array([0.82, 0.87, 0.77, 0.96, 0.75, 0.83, 0.87, 0.81])
    print(f"Intervalle de confiance : {interv_conf_inf_30(data, 0.05)}")

    print("Question 2.2")
    data = np.array([
    0.84, 0.87, 0.89, 0.73, 0.84, 0.81, 0.88, 0.85,
    0.89, 0.79, 0.79, 0.90, 0.59, 0.75, 0.67, 0.76,
    0.86, 0.88, 0.70, 0.75, 0.81, 0.77, 0.83, 0.84,
    0.71, 0.78, 0.59, 0.91, 0.74, 0.68, 0.77, 0.66,
    0.80, 0.74, 1.02, 0.91, 0.55, 0.84, 0.66, 0.77
    ])
    print(f"Intervalle de confiance : {interv_conf_grand_nombres(data, 0.05)}")
    
    print("\n")
    print("/////////////////////////////////////////////")
    print("PARTIE 3")
    print("Question 3.1")

    n = 1000
    data = np.array(
        ["Dupond"] * int(500) +
        ["Durand"] * int(250) +
        ["Duroc"] * int(50)
    )
    
    for confiance in [0.95, 0.99]:
        print(f"\nIntervalle de confiance à {confiance * 100:.0f} %")
        for candidat in np.unique(data):

            IC = interv_conf_prop_grand_echantillon(
                data, candidat, confiance, n
            )
            print(f"{candidat:<8} : [{IC[0]:.4f} ; {IC[1]:.4f}]")

    print("Question 3.2")
    #Formule du cours slide 144
    n_calc = np.ceil(((st.norm.ppf(1 - 0.05/2)/0.01)**2)*0.17*(1-0.17))
    print(f"Quantité n arrondi nécessaire : {n_calc}")
    print("\n")
    print("/////////////////////////////////////////////")
    print("PARTIE 4")
    print("Question 4.1")
    n = 50
    abime = 18
    data = np.array(
        ["Casque_abime"] * abime +
        ["casque_normal"] * (n - abime)
    )
    casques = np.unique(data)
    prop_data = np.sum(data == casques[0]) / n
    print(prop_data)
    print(f"{casques[0]:<8} : {interv_conf_prop_grand_echantillon(data, casques[0], 0.95, n)}")

    print("Question 4.2")
    n_calc = np.ceil(((st.norm.ppf(1 - 0.05/2)/0.01)**2)*prop_data*(1-prop_data))
    print(f"Quantité n arrondi nécessaire : {n_calc}")

    print("Question 4.3")

    alpha = 0.05
    erreur = 0.02

    p = 0.5  # valeur qui maximise p * (1 - p)
    z_alpha_2 = st.norm.ppf(1 - alpha / 2)

    n = np.ceil(
        (z_alpha_2 / erreur)**2 * p * (1 - p)
    )

    print("Valeur de p maximisant n :", p)
    print("Taille minimale de l'échantillon :", int(n))

    
