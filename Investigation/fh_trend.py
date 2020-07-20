import os 
import pickle
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


class FhTrend():
    def __init__(self, stft_path, formant_path, len=5):
        self.stft_path = stft_path 
        self.formant_path = formant_path
        self.len = len

    def combine_data(self, register='chest'):
        self.register = register
        n = 0
        for file in os.listdir(self.stft_path):
            if n >= self.len:
                break
            str_ls = file.split('_')
            if str_ls[-2] == register:
                n += 1
                if n == 1:
                    # load stft 
                    self.prev_stft = pickle.load(open(os.path.join(self.stft_path, file), 'rb'))
                    # load formants
                    self.prev_fs = pickle.load(open(os.path.join(self.formant_path, 'formant'+file[4:]), 'rb'))
                    self.prev_fs = np.array(self.prev_fs)
                else:
                    self.stft = pickle.load(open(os.path.join(self.stft_path, file), 'rb'))
                    self.prev_stft = np.concatenate((self.prev_stft, self.stft), axis=1)
                    self.fs = pickle.load(open(os.path.join(self.formant_path, 'formant'+file[4:]), 'rb'))
                    self.fs = np.array(self.fs)
                    self.prev_fs = np.concatenate((self.prev_fs, self.fs), axis=1)
            else:
                continue

        self.stft = self.prev_stft
        self.fs = self.prev_fs
        self.fs[self.fs == 0] = None

    def plot(self, show=True):
        self.f0 = self.fs[0]
        self.h2 = self.fs[1]
        self.h3 = self.fs[2]
        self.h4 = self.fs[3]
        self.f1 = self.fs[4]
        self.f2 = self.fs[5]
        self.f3 = self.fs[6]
        self.f4 = self.fs[7]
        self.time_len = np.arange(self.fs.shape[1])

        plt.figure(figsize=(10, 8))
        # ploting for f0 and harmonics
        plt.subplot(311)
        plt.plot(self.time_len, self.f0, label='f0')
        plt.plot(self.time_len, self.h2, label='h2')
        plt.plot(self.time_len, self.h3, label='h3')
        plt.plot(self.time_len, self.h4, label='h4')
        plt.grid()
        plt.xlabel("Time [s]")
        plt.ylabel("Magnitude")
        plt.legend(loc='upper left')

        # plotting for f1, f2, f3, f4
        plt.subplot(312)
        plt.plot(self.time_len, self.f1, label='f1')
        plt.plot(self.time_len, self.f2, label='f2')
        plt.plot(self.time_len, self.f3, label='f3')
        plt.plot(self.time_len, self.f4, label='f4')
        plt.grid()
        plt.xlabel("Time [s]")
        plt.ylabel("Magnitude")
        plt.legend(loc='upper left')

        # plotting stft for comparison
        plt.subplot(313)
        librosa.display.specshow(self.stft, x_axis='time', y_axis='linear')
        
        plt.savefig('fh_visuals/%s' % self.register)
        if show:
            plt.show()
        else:
            plt.close()
