import os


def check_if_num(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False


def change_numbering(data_path):
    # change numbering to 3-digit numbering e.g. 001, 021, 103
    for file in os.listdir(data_path):
        if check_if_num(file[-6]):
            os.rename(os.path.join(data_path, file), os.path.join(data_path, file[:-6] + '0' + file[-6:]))
        elif check_if_num(file[-7]):
            pass
        else:
            os.rename(os.path.join(data_path, file), os.path.join(data_path, file[:-5] + '00' + file[-5:]))
 

def get_n_registers(data_path):
    # Get the respective number of samples per register
    n_chest = 0
    n_mix = 0
    n_head = 0
    n_falsetto = 0
    n_whistle = 0
    n_controversial = 0

    for file in os.listdir(data_path):
        str_ls = file.split('_')
        if str_ls[-2] == 'chest':
            n_chest += 1
        elif str_ls[-2] == 'mixed':
            n_mix += 1
        elif str_ls[-2] == 'head':
            n_head += 1
        elif str_ls[-2] == 'falsetto':
            n_falsetto += 1
        elif str_ls[-2] == 'controversial':
            n_controversial += 1
        elif str_ls[-2] == 'whistle':
            n_whistle += 1

    return [n_chest, n_mix, n_head, n_falsetto, n_whistle, n_controversial]
        
