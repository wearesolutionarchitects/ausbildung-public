import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import numpy as np

abtastrate, werte = wf.read("tada.wav")
print(f"Abtastrate: {abtastrate} Werte / sec.")
print("Anzahl Werte:", werte.shape[0])
length = werte.shape[0] / abtastrate
print(f"Länge: {round(length,2)} sec.")

zeit = np.linspace(0, length, werte.shape[0])
plt.plot(zeit, werte[:, 0], label="Links")
plt.plot(zeit, werte[:, 1], label="Rechts")
plt.legend()
plt.xlabel("sec.")
plt.ylabel("Amplitude")
plt.show()
