from tkinter import S
from tagiofuns.load_nc import load_nc
from tagiofuns.save_nc import save_nc
from tagiofuns.add_nc import add_nc
from tagiofuns.remove_nc import remove_nc
from constants.depth2pressure import depth2pressure
# from load_nc import load_nc
import matplotlib.pyplot as plt


X = load_nc('test_data/testset3')
# print(X['A']['data'])
# # print(X)
# plt.plot(X['P']['data'])
# plt.show()
N = depth2pressure(1000, 27)
print(N)
