import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# load datasets
sentiment = pd.read_csv("sentiment.csv")
trades = pd.read_csv("trades.csv")


# print column names (very important for debugging)
print(sentiment.columns)
print(trades.columns)


# convert sentiment date column to datetime
sentiment['date'] = pd.to_datetime(sentiment['date'])

# convert trade timestamp column to datetime
trades['Timestamp IST'] = pd.to_datetime(
    trades['Timestamp IST'],
    dayfirst=True,
    format='mixed',
    errors='coerce'
)
print("Null timestamps:", trades['Timestamp IST'].isnull().sum())

# create common date column in both datasets
sentiment['Date'] = sentiment['date'].dt.date
trades['Date'] = trades['Timestamp IST'].dt.date


# create win column based on pnl
trades['win'] = np.where(trades['Closed PnL'] > 0 , 1 , 0)

# create long indicator
trades['long'] = np.where(trades['Side'] == "BUY" , 1 , 0)


# daily pnl per trader
daily_pnl = trades.groupby(['Account','Date'])['Closed PnL'].sum().reset_index()

# trade frequency
num_trades = trades.groupby(['Account','Date']).size().reset_index(name='num_trades')

# avg trade size
avg_size = trades.groupby(['Account','Date'])['Size USD'].mean().reset_index(name='avg_size')

# win rate
win_rate = trades.groupby(['Account','Date'])['win'].mean().reset_index(name='win_rate')

# long ratio
long_ratio = trades.groupby(['Account','Date'])['long'].mean().reset_index(name='long_ratio')


# merge all metrics
df = daily_pnl.merge(num_trades,on=['Account','Date'])
df = df.merge(avg_size,on=['Account','Date'])
df = df.merge(win_rate,on=['Account','Date'])
df = df.merge(long_ratio,on=['Account','Date'])


# merge sentiment
df = df.merge(sentiment[['Date','classification']],on='Date',how='left')


# fear vs greed performance
summary = df.groupby('classification').agg({
    'Closed PnL':'mean',
    'win_rate':'mean',
    'num_trades':'mean',
    'avg_size':'mean'
})

print(summary)


# segmentation
df['freq_segment'] = np.where(df['num_trades'] > df['num_trades'].median(),
                              'Frequent','Infrequent')

df['consistency'] = np.where(df['win_rate'] > 0.55,
                             'Consistent','Inconsistent')


# charts
sns.boxplot(x='classification',y='Closed PnL',data=df)
plt.show()

sns.barplot(x='classification',y='num_trades',data=df)
plt.show()

sns.barplot(x='classification',y='avg_size',data=df)
plt.show()


# save outputs
df.to_csv("final_dataset.csv",index=False)
summary.to_csv("summary.csv")

print("✅ Assignment analysis completed")