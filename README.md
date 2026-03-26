# Trader Performance vs Market Sentiment Analysis

## Objective
The objective of this project is to analyze how Bitcoin market sentiment (Fear vs Greed) influences trader behaviour and trading performance on the Hyperliquid platform.

## Dataset
The analysis uses two datasets:
- Bitcoin Market Sentiment dataset containing daily Fear/Greed classification
- Historical Trader dataset containing trade execution details such as price, size, side, and realized PnL

## Methodology
- Cleaned and validated both datasets by checking missing values and duplicates  
- Converted timestamps and aligned data at daily level  
- Engineered key behavioural and performance metrics such as:
  - Daily realized PnL per trader  
  - Win rate  
  - Trade frequency  
  - Average trade size  
- Merged sentiment data with trader metrics for comparative analysis  
- Performed segmentation of traders based on trading frequency and performance consistency  
- Visualized behavioural and performance differences across sentiment regimes  

## Key Insights
- Trader profitability and participation generally increase during Greed sentiment periods  
- Traders take larger risks and execute more trades in bullish market conditions  
- Frequent traders show higher return variability, indicating greater sensitivity to sentiment  
- Disciplined traders maintain relatively stable performance across different sentiment regimes  

## Strategy Recommendations
- Reduce trade frequency and position size during Fear periods to manage downside risk  
- Increase participation cautiously during Greed periods while avoiding excessive leverage  
- Use behaviour-based trading strategies by adapting exposure based on trader profile and sentiment cycles  

## Conclusion
Market sentiment plays an important role in shaping trader behaviour and performance.  
Adopting sentiment-aware and risk-adjusted trading strategies can help improve decision-making and trading outcomes in volatile crypto markets.

## How to Run
1. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn