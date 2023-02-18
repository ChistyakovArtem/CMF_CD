# CMF_CD
My work on a project "Credit derivatives and their application: introduction to the macro credit markets" in the Center of Mathematical Finances.

# Results
- Made a **Low Frequency pair trading** using data from multiple sources with **Sharpe ratio = 1.45** and **APY = 22%** from 2019-01-01 to 2021-12-30.

# Strategy description
- I use a lot of **external data** to predict the return of 3 CDS (Itraxx Main, Itraxx Crossover and CDX_IG) and 2 Equity Indexed (SnP 500 and Euro Stoxx). The **correlation with return** was respectively (0.28, 0.26, 0.07, -0.01, 0.25).
- Itraxx Main and Itraxx Crossover are highly correlated (0.98), so I decided to trade only Itraxx Main - Euro Stoxx.
- Multiple strategies included Itraxx Main trading, Euro Stoxx trading and pair trading based on return predictions.

# Data Sources
- As I said - I used many external real life data for return predictions. Here are the sources.
1) Commodities prices - https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm
2) Forex - api.exchangerate.host; DXY (dollar price) - https://www.wsj.com/market-data/quotes/index/DXY/historical-prices
3) Different countries 1 year bonds rates
https://www.investing.com/rates-bonds/uk-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/indonesia-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/philippines-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/u.s.-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/china-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/brazil-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/south-korea-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/france-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/germany-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/india-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/canada-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/australia-1-year-bond-yield-historical-data

https://www.investing.com/rates-bonds/japan-1-year-bond-yield-historical-data

4) Stock Indices

https://www.macrotrends.net/charts/stock-indexes

Bloomberg wants me to pay :(

https://www.statista.com/statistics/270126/largest-stock-exchange-operators-by-market-capitalization-of-listed-companies
