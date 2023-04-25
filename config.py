import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, filtfilt, butter
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

def lowpass(data, sample_rate, cutoff_freq, filter_order, title):

    # Generate the filter coefficients using the firwin function
    nyquist_rate = sample_rate / 2
    filter_coeffs = firwin(filter_order, cutoff_freq/nyquist_rate)
    file_name = 'lp_' + str(filter_order) + '.eps'

    # Apply the filter to the test signal
    filtered_signal = lfilter(filter_coeffs, 1, data)

    # Plot the original and filtered signals
    plt.figure(figsize=(15, 5))
    plt.specgram(filtered_signal, Fs=sample_rate, vmin=-20, vmax=50)
    plt.title(title)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.savefig(file_name, format='eps', dpi = 50)
    plt.show()






def bandpass(data, sample_rate, cutoff_freq1, cutoff_freq2, filter_order, title):

    # Generate the filter coefficients using the firwin function
    cutoff_freq3 = [cutoff_freq1[0] / (0.5*sample_rate), cutoff_freq1[1] / (0.5*sample_rate)]
    cutoff_freq4 = [cutoff_freq2[0] / (0.5 * sample_rate), cutoff_freq2[1] / (0.5 * sample_rate)]
    num_taps = filter_order
    b1 = firwin(num_taps, cutoff_freq3, pass_zero=False)
    b2 = firwin(num_taps, cutoff_freq4, pass_zero=False)

    # Apply the filter to the data
    filtered_signal1 = filtfilt(b1, 1, data)
    filtered_signal2 = filtfilt(b2, 1, data)
    n_transient = num_taps - 1
    filtered_signal1 = filtered_signal1[n_transient:]
    filtered_signal2 = filtered_signal2[n_transient:]
    filtered_signal = filtered_signal1 + filtered_signal2

    file_name = 'bp_' + str(filter_order) + '.eps'
    # Plot the original and filtered signals
    plt.figure(figsize=(15, 5))
    plt.specgram(filtered_signal, Fs=sample_rate, vmin=-20, vmax=50)
    plt.title(title)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.savefig(file_name, format='eps', dpi = 50)
    plt.show()


def irbutter(data, sample_rate, cutoff_freq1, filter_order, title):


    b, a = butter(filter_order, cutoff_freq1 / (sample_rate / 2), btype='lowpass', analog=False)

    # Apply filter to signal
    filtered_signal = filtfilt(b, a, data)
    file_name = 'butt_' + str(filter_order) + '.eps'
    # Plot the original and filtered signals
    plt.figure(figsize=(15, 5))
    plt.specgram(filtered_signal, Fs=sample_rate, vmin=-20, vmax=50)
    plt.title(title)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.savefig(file_name, format='eps', dpi = 50)
    plt.show()


def oversample(data, sample_rate, freq):
    t = np.arange(len(data)) / sample_rate
    t_new = np.arange(0, t[-1], 1/8000)
    y_new = np.interp(t_new, t, data)
    nyquist = sample_rate / 2.0
    cutoff = 8000 / nyquist
    b, a = butter(8, cutoff)
    y_filtered = filtfilt(b, a, y_new)

    return y_filtered, t_new

def signal_segment(data, N):
    m = 2 ** N
    segments = []
    for i in range(0, len(data), m):
        segment = data[i:i+m]
        if len(segment) == m:
            segments.append(segment)

    segments = np.array(segments)

    return segments

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even + factor[:N//2] * odd, even + factor[N//2:] * odd])
