Stock Portfolio and Sales Data Analysis

Team Members :
1. Shrey Soni 
2. Naisheel Patel 
3. Suhani Patel 
4. Dhyani Dave 
5. Prince Patel 

Overview
This application analyzes:
1.	Stock portfolios for risk, return, and performance metrics.
2.	Sales data for insights into total sales by item type.
It is built using Python libraries such as pandas, numpy, yfinance, matplotlib, and streamlit. The app allows users to input stock portfolios and upload sales data for analysis via an interactive interface.
________________________________________
Features
1. Stock Portfolio Analysis
•	Input: Users provide a stock portfolio as ticker symbols and shares (e.g., AAPL:10, MSFT:5).
•	Metrics Calculated: 
o	Expected Annual Returns (per stock and portfolio)
o	Annualized Volatility (per stock and portfolio)
o	Sharpe Ratio (portfolio)
•	Risk-Return Visualization: A scatterplot showing individual stock risk-return profiles and the overall portfolio performance.
2. Sales Data Analysis
•	Input: Users upload a CSV file containing sales data.
•	Analysis Performed: 
o	Total sales aggregated by Item_Type.
o	Visualization of sales distribution using a bar chart.
o	Tabular display of aggregated results.
________________________________________
How to Use
Prerequisites
Install the required Python packages:
pip install pandas numpy yfinance matplotlib streamlit
Running the Application
1.	Save the script to a .py file (e.g., app.py).
2.	Start the Streamlit application by running: 
3.	streamlit run app.py
4.	Open the application in your browser (Streamlit will provide the link).
Input Instructions
Stock Portfolio Analysis
•	Enter your portfolio in the following format: 
•	Ticker:Shares, e.g., AAPL:10, MSFT:5, GOOGL:8, AMZN:3
•	Click the Analyze Portfolio button to view metrics and visualizations.
Sales Data Analysis
•	Upload a sales data CSV file with at least the following columns: 
o	Item_Type
o	Item_Outlet_Sales
•	View the analysis, which includes: 
o	Bar chart of total sales by item type.
o	Tabular display of aggregated sales data.
________________________________________
Code Details
Modules Used
1.	pandas: Data manipulation and analysis.
2.	numpy: Numerical computations for portfolio analysis.
3.	yfinance: Fetching historical stock data.
4.	matplotlib: Risk-return scatterplot.
5.	streamlit: Interactive user interface for inputs and outputs.
Functions
1. analyze_portfolio(portfolio)
•	Fetches historical stock data using yfinance.
•	Calculates: 
o	Daily returns.
o	Expected returns and volatility (annualized).
o	Portfolio return and volatility using weights.
o	Sharpe ratio (assuming a risk-free rate of 0.01).
•	Returns: 
o	Expected returns (per stock).
o	Volatility (per stock).
o	Portfolio metrics (return, volatility, Sharpe ratio).
2. analyze_sales_data(sales_data)
•	Aggregates total sales by Item_Type.
•	Returns: 
o	Sorted sales totals.
________________________________________
Notes
Portfolio Analysis Assumptions
•	Start Date: 2020-01-01
•	End Date: 2023-01-01
•	Risk-free rate for Sharpe Ratio: 0.01
Known Issues
•	Ensure the portfolio input format is correct. Invalid inputs may cause errors.
•	Uploaded sales data must include the required columns (Item_Type, Item_Outlet_Sales).
________________________________________
Example Usage
Portfolio Input
AAPL:10, MSFT:5, GOOGL:8, AMZN:3
Expected output includes:
•	Individual stock metrics (returns, volatility).
•	Portfolio metrics (expected return, volatility, Sharpe ratio).
•	Risk vs. Return scatterplot.
Sales Data Input
Example CSV structure:
Item_Type	Item_Outlet_Sales
Fruits	12345.67
Snacks	9876.54
Output includes:
•	Total sales bar chart.
•	Tabular summary of total sales.
________________________________________

