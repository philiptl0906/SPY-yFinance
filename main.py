import yfinance as yf
import pandas as pd

spy = yf.Ticker("SPY")

# Get the historical market data
df =pd.DataFrame(spy.history(period="1y"))

# export to excel
try:
    df[['Open', 'High', 'Low', 'Close', 'Volume']].to_csv('SPY.csv', mode='w+', index= True)

except:
   print("WARNING!")
   print("File not updated. Please close the CSV file before running this script")