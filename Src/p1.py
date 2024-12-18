import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

# Function to fetch stock data and calculate metrics
def analyze_portfolio(portfolio):
    # Fetch historical data for the stocks in the portfolio
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    data = yf.download(list(portfolio.keys()), start=start_date, end=end_date)['Adj Close']

    # Calculate daily returns
    returns = data.pct_change().dropna()

    # Calculate expected returns and volatility
    expected_returns = returns.mean() * 252  # Annualized return
    volatility = returns.std() * np.sqrt(252)  # Annualized volatility

    # Calculate portfolio return and volatility
    weights = np.array(list(portfolio.values())) / sum(portfolio.values())
    portfolio_return = np.dot(weights, expected_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))

    # Calculate Sharpe Ratio (assuming a risk-free rate of 0.01)
    risk_free_rate = 0.01
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    return expected_returns, volatility, portfolio_return, portfolio_volatility, sharpe_ratio

# Function to analyze sales data
def analyze_sales_data(sales_data):
    total_sales = sales_data.groupby('Item_Type')['Item_Outlet_Sales'].sum().sort_values(ascending=False)
    return total_sales

# Streamlit app
st.title("Stock Portfolio and Sales Data Analysis")

# Portfolio input
st.header("Stock Portfolio Analysis")
portfolio_input = st.text_area("Enter your portfolio (format: Ticker:Shares, e.g., AAPL:10, MSFT:5)", "AAPL:10, MSFT:5, GOOGL:8, AMZN:3")
if st.button("Analyze Portfolio"):
    portfolio = {item.split(':')[0].strip(): int(item.split(':')[1].strip()) for item in portfolio_input.split(',')}
    expected_returns, volatility, portfolio_return, portfolio_volatility, sharpe_ratio = analyze_portfolio(portfolio)

    st.subheader("Expected Returns")
    st.write(expected_returns)

    st.subheader("Volatility")
    st.write(volatility)

    st.write(f"Portfolio Expected Return: {portfolio_return:.2%}")
    st.write(f"Portfolio Volatility: {portfolio_volatility:.2%}")
    st.write(f"Sharpe Ratio: {sharpe_ratio:.2f}")

    # Plotting the risk-return profile
    fig, ax = plt.subplots()
    ax.scatter(volatility, expected_returns, marker='o')
    for i, txt in enumerate(portfolio.keys()):
        ax.annotate(txt, (volatility[i], expected_returns[i]), fontsize=12)
    ax.scatter(portfolio_volatility, portfolio_return, color='red', marker='*', s=200, label='Portfolio')
    ax.set_title('Risk vs Return')
    ax.set_xlabel('Volatility (Risk)')
    ax.set_ylabel('Expected Return')
    ax.legend()
    ax.grid()
    st.pyplot(fig)

# Sales data input
st.header("Sales Data Analysis")
sales_file = st.file_uploader("Upload your sales data CSV file", type=["csv"])

if sales_file is not None:
    sales_data = pd.read_csv(sales_file)
    st.write("Sales Data:")
    st.write(sales_data.head())

    # Analyze sales data
    total_sales = analyze_sales_data(sales_data)

    st.subheader("Total Sales by Item Type")
    st.bar_chart(total_sales)

    # Display total sales in a table
    st.write("Total Sales Table:")
    st.dataframe(total_sales)

# Run the app
if _name_ == "_main_":
    st.write("Streamlit app is running...")
