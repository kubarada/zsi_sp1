import scipy.io as sc
import matplotlib.pyplot as plt
import numpy as np

import config as cnf

INPUT_FILE = 'C:/Users/qradj/OneDrive - AIMTEC a. s/Desktop/zsi_sp1./veta.wav'

rate, data = sc.wavfile.read(INPUT_FILE)

# Compute the power spectrum of the audio signal
# Use a window size of 1024 and 50% overlap
win = 1024
hop_length = win // 2
spec = np.abs(np.fft.rfft(data, n=win, axis=0))
freqs = np.fft.rfftfreq(win, d=1/rate)
t = np.arange(0, len(data)) / rate
print('Lenght of audiofile: ' + str(t[-1]) + ' s')

# ploting audio wave
cnf.plot(t, data, ['Time [s]', 'Signal value'], lim = [0, t[-1], -31000, 25000],  title = 'Časový vývoj signálu')

# ploting the spectrum of audio
cnf.plot(freqs, spec, ["Frequency [Hz]", "Magnitude [dB]"], lim = [0, 22000, 0, 460000], title = 'Spektrum signálu')

plt.figure(figsize=(15, 5))
plt.specgram(data, Fs=rate, vmin=-20, vmax=50)
plt.title('Spektogram')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.show()


cnf.lowpass(data, sample_rate = rate, cutoff_freq = 5600, filter_order=170) 