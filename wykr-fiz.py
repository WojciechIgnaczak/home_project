
import matplotlib.pyplot as plt
import numpy as np

N= int(input('Podaj ilość ramek: '))
B = float(input("Podaj wartość indukcji magnetycznej B[T]: "))
S = float(input("Podaj wartość powierzchni S[m^2]: "))
Omega = float(input("Podaj wartość Omega [rad/s]: "))

if Omega<1:
    i=8
elif Omega<5:
    i=4
elif Omega<10:
    i=1
elif Omega<20:
    i=0.5
elif Omega<50:
    i=0.1
elif Omega<100:
    i=0.1
else:
    i=0.08

czas = np.linspace(0, i*np.pi, 1000)#zmiana wywietlania ilosci okresow
napięcie = N * B * S * Omega * np.sin(Omega * czas)
czas_w_sekundach = czas / Omega  # Konwersja czasu z radianów na sekundy


# Znalezienie indeksów, gdzie napięcie zmienia znak
zmiana_znaku = np.where(np.diff(np.sign(napięcie)))[0]

# Znalezienie dokładniejszych czasów przecięcia z osią OX
dokladne_czasy = []
for idx in zmiana_znaku:
    czas_pierwszy = czas_w_sekundach[idx]
    czas_drugi = czas_w_sekundach[idx + 1]
    if np.sign(napięcie[idx]) != np.sign(napięcie[idx + 1]):
        zero_crossing = np.interp(0, [napięcie[idx], napięcie[idx + 1]], [czas_pierwszy, czas_drugi])
        dokladne_czasy.append(zero_crossing)

# Sprawdzenie ostatniego punktu, czy jest równy zero
if napięcie[-1] == 0:
    dokladne_czasy.append(czas_w_sekundach[-1])

# Rysowanie wykresu
plt.plot(czas_w_sekundach, napięcie)
plt.title('Wykres napięcia od czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Napięcie [V]')
plt.grid(True)

# Umieszczenie wartości czasu, gdy napięcie jest bliskie zera
for czas_zero_wartosc in dokladne_czasy:
    plt.text(czas_zero_wartosc, 0, f'{czas_zero_wartosc:.4f} s', ha='center', va='bottom')#zeby zmienic dokladnosc zmien 4f na cos

# Umieszczenie wartości maksymalnej i minimalnej na wykresie
if Omega > 5:
    plt.text(0.2, np.max(napięcie), f'BSω: {np.max(napięcie):.2f} V', ha='right', va='bottom')
    plt.text(0.2, np.min(napięcie), f'-BSω: {np.min(napięcie):.2f} V', ha='right', va='top')
else:
    plt.text(1, np.max(napięcie), f'BSω: {np.max(napięcie):.2f} V', ha='right', va='bottom')
    plt.text(1, np.min(napięcie), f'-BSω: {np.min(napięcie):.2f} V', ha='right', va='top')

# Osie x i y w punkcie (0,0)
plt.axhline(0, color='black', linewidth=2)  # Oś y w punkcie 0
plt.axvline(0, color='black', linewidth=2)  # Oś x w punkcie 0

plt.show()