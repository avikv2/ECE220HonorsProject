# Import the plotting library 
import matplotlib.pyplot as plt 
 
# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook 
import yfinance as yf   
 

ticker = 'AAPL'
while (ticker != 'q'):
    data = yf.download(ticker,'2016-01-01','2021-05-31', auto_adjust=True)
    data.Close.plot() 
    plt.grid() 
    plt.show()  
    ticker = input("type in a a ticker name or q to quit: ")
