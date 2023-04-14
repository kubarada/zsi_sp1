import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter
import numpy as np


# prostě plotovací fce, abych nemusel milionkrát psát plt., plt.,.....
def plot(x, y, legend = ['x', 'y'], lim = ['', '', '', ''], title = 'Doplnit title!'):

    plt.figure()
    plt.plot(x, y)
    plt.xlabel(legend[0])
    plt.title(title)
    plt.grid()
    plt.ylabel(legend[1])
    if lim[0] != '':
        plt.xlim(float(lim[0]), float(lim[1]))
        plt.ylim(float(lim[2]), float(lim[3]))
    plt.show()

def lowpass(data, sample_rate, cutoff_freq, filter_order):

    # Generate the filter coefficients using the firwin function
    nyquist_rate = sample_rate / 2
    filter_coeffs = firwin(filter_order, cutoff_freq/nyquist_rate)


    # Apply the filter to the test signal
    filtered_signal = lfilter(filter_coeffs, 1, data)

    # Plot the original and filtered signals
    plt.figure(figsize=(15, 5))
    plt.specgram(filtered_signal, Fs=sample_rate, vmin=-20, vmax=50)
    plt.title('Spektogram')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.show()
