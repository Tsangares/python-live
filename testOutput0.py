# make the imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import io, signal # we will also import the signal module, from s
def plot_spectrogram(spg, t, f, freq_lims=[0,100], plot_db=False):
    """
                    Utility function for plotting the spectrogram for you.

                                        spg: spectrogram, 2D real-numbered array, dimensions are [frequency x time]
                                                                t: time axis of spectrogram
                                                                                            f: frequency axis of spectrogram
                                                                                                                            freq_lims (optional): limits the frequency axis, defaults to 0-100Hz
                                                                                                                                                                """
                                                                                                                                                                                                        plt.figure(figsize=(15,4))
                                                                                                                                                                                                                                                    if plot_db:
                                                                                                                                                                                                                                                        plt.imshow(10*np.log10(spg), aspect='auto', extent=[t[0], t[-1], f[-1], f[0]])
                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        plt.imshow(spg, aspect='auto', extent=[t[0], t[-1], f[-1], f[0]])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    plt.xlabel('Time'); plt.ylabel('Frequency(Hz)');
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    plt.ylim(freq_lims)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        plt.colorbar()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                plt.tight_layout()


T, fs = 20, 1000
t = np.arange(0,T,1/fs)
# simulate a signal
# refer to the function documentation for f0, t1, f1
sig = signal.chirp(t, f0=10, t1=20,f1=30)

# plot it
plt.figure(figsize=(15,3))
plt.plot(t,sig)
