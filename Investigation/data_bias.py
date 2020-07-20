import os


def check_if_num(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False


class StatisticsCounter():
    def __init__(self, data_path):
        self.data_path = data_path

    def change_numbering(self):
        # change numbering to 3-digit numbering e.g. 001, 021, 103
        for file in os.listdir(self.data_path):
            if check_if_num(file[-6]):
                os.rename(os.path.join(self.data_path, file), os.path.join(self.data_path, file[:-6] + '0' + file[-6:]))
            elif check_if_num(file[-7]):
                pass
            else:
                os.rename(os.path.join(self.data_path, file), os.path.join(self.data_path, file[:-5] + '00' + file[-5:]))
    

    def get_n_registers(self):
        # Get the respective number of samples per register
        self.n_chest = 0
        self.n_mix = 0
        self.n_head = 0
        self.n_falsetto = 0
        self.n_whistle = 0
        self.n_controversial = 0

        for file in os.listdir(self.data_path):
            str_ls = file.split('_')
            if str_ls[-2] == 'chest':
                self.n_chest += 1
            elif str_ls[-2] == 'mixed':
                self.n_mix += 1
            elif str_ls[-2] == 'head':
                self.n_head += 1
            elif str_ls[-2] == 'falsetto':
                self.n_falsetto += 1
            elif str_ls[-2] == 'controversial':
                self.n_controversial += 1
            elif str_ls[-2] == 'whistle':
                self.n_whistle += 1

        return [self.n_chest, self.n_mix, self.n_head,
                self.n_falsetto, self.n_whistle, self.n_controversial]

    def show_n_registers(self):
        print('Statisitics:\n'
                'Chest: %s\n'
                'Mixed: %s\n'
                'Head: %s\n'
                'Falsetto: %s\n'
                'Whistle: %s\n'
                'Controversial: %s'
                % (self.n_chest, self.n_mix, self.n_head, self.n_falsetto, self.n_whistle, self.n_controversial))
        
