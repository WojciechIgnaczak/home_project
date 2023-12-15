import matplotlib.pyplot as plt
import numpy as np

def generuj_wykres(N, B, S, Omega):
    i = 8 if Omega < 1 else 4 if Omega < 5 else 1 if Omega < 10 else 0.5 if Omega < 20 else 0.1 if Omega < 50 else 0.1 if Omega < 100 else 0.08

    czas = np.linspace(0, i * np.pi, 1000)
    napięcie = N * B * S * Omega * np.sin(Omega * czas)
    czas_w_sekundach = czas / Omega

    zmiana_znaku = np.where(np.diff(np.sign(napięcie)))[0]

    dokladne_czasy = []
    for idx in zmiana_znaku:
        czas_pierwszy = czas_w_sekundach[idx]
        czas_drugi = czas_w_sekundach[idx + 1]
        if np.sign(napięcie[idx]) != np.sign(napięcie[idx + 1]):
            zero_crossing = np.interp(0, [napięcie[idx], napięcie[idx + 1]], [czas_pierwszy, czas_drugi])
            dokladne_czasy.append(zero_crossing)

    if napięcie[-1] == 0:
        dokladne_czasy.append(czas_w_sekundach[-1])

    plt.plot(czas_w_sekundach, napięcie, label=f'N={N}, B={B}, S={S}, Omega={Omega}')
    plt.title('Wykres napięcia od czasu')
    plt.xlabel('Czas [s]')
    plt.ylabel('Napięcie [V]')
    plt.grid(True)

    for czas_zero_wartosc in dokladne_czasy:
        plt.text(czas_zero_wartosc, 0, f'{czas_zero_wartosc:.4f} s', ha='center', va='bottom')

    if Omega > 5:
        plt.text(0.2, np.max(napięcie), f'BSω: {np.max(napięcie):.2f} V', ha='right', va='bottom')
        plt.text(0.2, np.min(napięcie), f'-BSω: {np.min(napięcie):.2f} V', ha='right', va='top')
    else:
        plt.text(1, np.max(napięcie), f'BSω: {np.max(napięcie):.2f} V', ha='right', va='bottom')
        plt.text(1, np.min(napięcie), f'-BSω: {np.min(napięcie):.2f} V', ha='right', va='top')

    plt.axhline(0, color='black', linewidth=2)
    plt.axvline(0, color='black', linewidth=2)

# Pierwszy wykres
N1 = int(input('Podaj ilość ramek (wykres 1): '))
B1 = float(input("Podaj wartość indukcji magnetycznej B[T] (wykres 1): "))
S1 = float(input("Podaj wartość powierzchni S[m^2] (wykres 1): "))
Omega1 = float(input("Podaj wartość Omega [rad/s] (wykres 1): "))
generuj_wykres(N1, B1, S1, Omega1)

# Drugi wykres
N2 = int(input('Podaj ilość ramek (wykres 2): '))
B2 = float(input("Podaj wartość indukcji magnetycznej B[T] (wykres 2): "))
S2 = float(input("Podaj wartość powierzchni S[m^2] (wykres 2): "))
Omega2 = float(input("Podaj wartość Omega [rad/s] (wykres 2): "))
generuj_wykres(N2, B2, S2, Omega2)

plt.legend()
plt.show()
