import matplotlib.pyplot as plt
import numpy as mp
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers = 'MSFT', period = '5d', interval = '5m')

plt.plot(data)

plt.show()



