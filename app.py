from tkinter import S
from tagiofuns.load_nc import load_nc
from tagiofuns.save_nc import save_nc
from tagiofuns.add_nc import add_nc
from tagiofuns.remove_nc import remove_nc
from constants.sound_speed import sound_speed
# from load_nc import load_nc
import matplotlib.pyplot as plt


X = load_nc('test_data/testset3')
# print(X['A']['data'])
# # print(X)
# plt.plot(X['P']['data'])
# plt.show()
N = sound_speed(8, 1000, 34)
print(N)
