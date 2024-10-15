import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler

class Matrix:
    def __init__(self):
        self.symbols = []
        self.data = {
            "ROE (%)": [], 
            "Performance 5Y (%)": [],
            "5 Year Average Dividend Yield (%)": [],
            "Market Capitalization": [],
            "Debt-to-Equity Ratio": [],
            "Beta": [],
            "Volatility 5Y (%)": []
        }
        self.correlation_matrix = None
        self.port_stock_quantity = None
        self.risk_value = None

    def add_port(self, port):
        self.port_stock_quantity = len(port)

        for stock in port:
            self.symbols.append(stock[0])
            self.data["ROE (%)"].append(stock[4])
            self.data["Performance 5Y (%)"].append(stock[8])
            self.data["5 Year Average Dividend Yield (%)"].append(stock[9])
            self.data["Market Capitalization"].append(stock[10])
            self.data["Debt-to-Equity Ratio"].append(stock[11])
            self.data["Beta"].append(stock[12])
            self.data["Volatility 5Y (%)"].append(stock[13])

    def find_matrix_correlation(self):
        df = pd.DataFrame(self.data)

        scaler = RobustScaler()

        normalized_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

        stocks = pd.DataFrame({
            self.symbols[i]: normalized_df.iloc[i] for i in range(len(self.symbols))
        }, index=normalized_df.columns)

        self.correlation_matrix = stocks.corr()

        temp_correlation_ematrix = self.correlation_matrix.copy()
        self.calculate_risk(temp_correlation_ematrix)

    def calculate_risk(self, correlation_matrix):
        sum_all_risk_value = 0
        sum_table_row = 0
        tablearr = correlation_matrix.to_numpy()

        for i in range(self.port_stock_quantity):
            sum_table_row = 0

            for j in range(self.port_stock_quantity):
                tablearr[i][j] = 5 * (tablearr[i][j] + 1) 
                sum_table_row += tablearr[i][j]

            sum_all_risk_value += sum_table_row / self.port_stock_quantity      

        self.risk_value = sum_all_risk_value / self.port_stock_quantity 

    def show_heatmap(self):
        plt.figure(figsize=(8, 6))
        plt.title("Portfolio Correlation Heatmap")
        sns.heatmap(self.correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.show()