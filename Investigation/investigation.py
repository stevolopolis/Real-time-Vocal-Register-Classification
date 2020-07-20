from data_bias import StatisticsCounter

data_path = 'D:/AI Project Group/VOCREG/DATA/Labelled_data/STFT_Jul20'

Stats = StatisticsCounter(data_path)
stats_ls = Stats.get_n_registers()
Stats.show_n_registers()
