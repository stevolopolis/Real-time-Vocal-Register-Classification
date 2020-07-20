from data_bias import StatisticsCounter
from stft_visualization import StftVisual
from fh_trend import FhTrend

stft_path = 'D:/AI Project Group/VOCREG/DATA/Labelled_data/STFT_Jul20'
formant_path = 'D:/AI Project Group/VOCREG/DATA/Labelled_data/Formants_Jul20'
registers = ['chest', 'mixed', 'head', 'falsetto', 'whistle', 'controversial']

Stats = StatisticsCounter(stft_path)
stats_ls = Stats.get_n_registers()
Stats.show_n_registers()

StftVis = StftVisual(stft_path, len=7)
FhVis = FhTrend(stft_path, formant_path, len=7)
for reg in registers:
    print('processing register: %s' % reg)
    StftVis.combine_stft(register=reg)
    StftVis.plot(show=False)
    FhVis.combine_data()
    FhVis.plot(show=False)