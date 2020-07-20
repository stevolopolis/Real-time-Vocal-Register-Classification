import os


def check_if_num(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False


n_chest = 0
n_mix = 0
n_head = 0
n_falsetto = 0
n_whistle = 0

data_path = 'D:/AI Project Group/VOCREG/DATA/Labelled_data/STFT_Jul20'

# change numbering to 3-digit numbering e.g. 001, 021, 103
for file in os.listdir(data_path):
    if check_if_num(file[-6]):
        os.rename(os.path.join(data_path, file), os.path.join(data_path, file[:-7] + '0' + file[-7:]))
    elif check_if_num(file[-7]):
        pass
    else:
        print(os.path.join(data_path, file[:-6] + '00' + file[-6:]))
        input()
        os.rename(os.path.join(data_path, file), os.path.join(data_path, file[:-6] + '00' + file[-6:]))
        