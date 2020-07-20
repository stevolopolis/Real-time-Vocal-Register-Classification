import os
import pickle
import librosa, librosa.display 
import matplotlib.pyplot as plt
import numpy as np


def show_stft(stft, file_name):
    print(stft.shape)
    plt.figure(figsize=(15, 5))
    librosa.display.specshow(stft, x_axis='time', y_axis='linear')
    plt.savefig('stft_visuals/%s' % file_name)
    plt.close()


def combine_stft(data_path, register='chest', len=5):
    n = 0
    for file in os.listdir(data_path):
        if n >= len:
            break
        str_ls = file.split('_')
        if str_ls[-2] == register:
            print(file)
            n += 1
            if n == 1:
                prev_stft = pickle.load(open(os.path.join(data_path, file), 'rb'))
            else:
                stft = pickle.load(open(os.path.join(data_path, file), 'rb'))
                prev_stft = np.concatenate((prev_stft, stft), axis=1)
        else:
            continue

    return prev_stft


data_path = 'D:/AI Project Group/VOCREG/DATA/Labelled_data/STFT_Jul20'
registers = ['chest', 'mixed', 'head', 'falsetto', 'whistle', 'controversial']

for reg in registers:
    stft = combine_stft(data_path, register=reg, len=10)
    show_stft(stft, reg)