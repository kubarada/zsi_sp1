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

# ploting audio wave
cnf.plot(t, data)

# ploting the spectrum of audio
cnf.plot(freqs, spec, ["Frequency (Hz)", "Magnitude"])


