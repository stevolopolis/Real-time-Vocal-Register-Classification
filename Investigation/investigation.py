from data_bias import StatisticsCounter
from stft_visualization import StftVisual

data_path = 'D:/AI Project Group/VOCREG/DATA/Labelled_data/STFT_Jul20'
registers = ['chest', 'mixed', 'head', 'falsetto', 'whistle', 'controversial']

Stats = StatisticsCounter(data_path)
stats_ls = Stats.get_n_registers()
Stats.show_n_registers()

StftVis = StftVisual(data_path, len=7)
for reg in registers:
    StftVis.combine_stft(register=reg)
    StftVis.plot(reg)