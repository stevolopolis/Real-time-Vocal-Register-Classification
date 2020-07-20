import os
import pickle
import librosa, librosa.display 
import matplotlib.pyplot as plt
import numpy as np

class StftVisual():
    def __init__(self, data_path, len=5):
        self.data_path = data_path
        self.len = len

    def combine_stft(self, register='chest'):
        self.register = register
        n = 0
        for file in os.listdir(self.data_path):
            if n >= self.len:
                break
            str_ls = file.split('_')
            if str_ls[-2] == register:
                n += 1
                if n == 1:
                    self.prev_stft = pickle.load(open(os.path.join(self.data_path, file), 'rb'))
                else:
                    stft = pickle.load(open(os.path.join(self.data_path, file), 'rb'))
                    self.prev_stft = np.concatenate((self.prev_stft, stft), axis=1)
            else:
                continue
    
    def plot(self, show=True):
        plt.figure(figsize=(15, 5))
        librosa.display.specshow(self.prev_stft, x_axis='time', y_axis='linear')
        plt.savefig('stft_visuals/%s' % self.register)
        if show:
            plt.show()
        else:
            plt.close()

