import scipy.io as sc
import matplotlib.pyplot as plt
import numpy as np
import config as cnf

INPUT_FILE = 'veta.wav'

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

# ploting spectogram
plt.figure(figsize=(15, 5))
plt.specgram(data, Fs=rate, vmin=-20, vmax=50)
plt.title('Spektrogram')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.show()
"""
# fir lowpass
cnf.lowpass(data, sample_rate = rate, cutoff_freq = 5700, filter_order=170, title = 'Spectrogram - filter order = 170')
cnf.lowpass(data, sample_rate = rate, cutoff_freq = 5700, filter_order=190,title = 'Spectrogram - filter order = 190')
cnf.lowpass(data, sample_rate = rate, cutoff_freq = 5700, filter_order=210,title = 'Spectrogram - filter order = 210')
cnf.lowpass(data, sample_rate = rate, cutoff_freq = 5700, filter_order=230,title = 'Spectrogram - filter order = 230')
cnf.lowpass(data, sample_rate = rate, cutoff_freq = 5700, filter_order=250,title = 'Spectrogram - filter order = 250')

# fir bandpass
cnf.bandpass(data, sample_rate = rate, cutoff_freq1= [1,5800], cutoff_freq2 = [6200, 19000],filter_order = 150,  title = 'Spectrogram - filter order = 150')
cnf.bandpass(data, sample_rate = rate, cutoff_freq1= [1,5800], cutoff_freq2 = [6200, 19000],filter_order = 175,  title = 'Spectrogram - filter order = 175')
cnf.bandpass(data, sample_rate = rate, cutoff_freq1= [1,5800], cutoff_freq2 = [6200, 19000],filter_order = 200,  title = 'Spectrogram - filter order = 200')
cnf.bandpass(data, sample_rate = rate, cutoff_freq1= [1,5800], cutoff_freq2 = [6200, 19000],filter_order = 250,  title = 'Spectrogram - filter order = 250')
cnf.bandpass(data, sample_rate = rate, cutoff_freq1= [1,5800], cutoff_freq2 = [6200, 19000],filter_order = 300,  title = 'Spectrogram - filter order = 300')

# iir lowpass butterwoth
cnf.irbutter(data, sample_rate = rate, cutoff_freq1 = 5700,filter_order = 5,  title = 'Spectrogram - filter order = 5')
cnf.irbutter(data, sample_rate = rate, cutoff_freq1 = 5700,filter_order = 10,  title = 'Spectrogram - filter order = 10')
cnf.irbutter(data, sample_rate = rate, cutoff_freq1 = 5700,filter_order = 15,  title = 'Spectrogram - filter order = 15')
cnf.irbutter(data, sample_rate = rate, cutoff_freq1 = 5700,filter_order = 20,  title = 'Spectrogram - filter order = 20')
cnf.irbutter(data, sample_rate = rate, cutoff_freq1 = 5700,filter_order = 25,  title = 'Spectrogram - filter order = 25')

"""
# převzorkování

data_re, t_new =  cnf.oversample(data, rate, 8000)
cnf.plot(t_new, data_re, ['Time [s]', 'Signal value'], lim = [0, t[-1], -31000, 25000],  title = 'Časový vývoj signálu')



