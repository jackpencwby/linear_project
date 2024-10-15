import numpy as np
import pandas as pd

class Vector:
    def __init__(self, index, pe_ratio, eps_growth, roe, dividend_yield, performance_years, performance):
        self.index = index
        self.pe_ratio = pe_ratio
        self.eps_growth = eps_growth
        self.roe = roe
        self.dividend_yield = dividend_yield
        self.performance_years = performance_years
        self.performance = performance
        self.user_vector = np.array([
            self.pe_ratio, 
            self.eps_growth, 
            self.roe, 
            self.dividend_yield, 
            self.performance
            ])
        
    def calculate_cosine_similarity(self, vector_u, vector_v):
        dot_product = np.dot(vector_u, vector_v)
        magnitude_a = np.linalg.norm(vector_u)
        magnitude_b = np.linalg.norm(vector_v)
    
        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (magnitude_a * magnitude_b)
    
    def filter_stocks(self):
        df = pd.read_excel("data\clean_data.xlsx")

        if df.empty:
            print("The Excel file not found.")
        else:
            if self.index == "All Indexes":
                filtered_df = df
            else:
                filtered_df = df[df["Index"] == self.index]
            
            if filtered_df.empty:
                print(f"No data found for Index : {self.index}")
            else:
                similarities = []
                for col, row in filtered_df.iterrows():
                    excel_vector = np.array([
                        row["PE Ratio"], 
                        row["EPS Growth (%)"], 
                        row["ROE (%)"],
                        row["Dividend Yield (%)"], 
                        row[f"Performance {self.performance_years}Y (%)"]
                    ])

                    similarity = self.calculate_cosine_similarity(self.user_vector, excel_vector)
                    similarities.append(similarity)

                filtered_df["Cosine Similarity"] = similarities

                top10_cosine_similarity = filtered_df.nlargest(10, "Cosine Similarity")

                columns_to_show = [
                    "Symbol",
                    "Company",
                    "PE Ratio",
                    "EPS Growth (%)",
                    "ROE (%)",
                    "Dividend Yield (%)",
                    f"Performance {self.performance_years}Y (%)", 
                    "Cosine Similarity",
                    "5 Year Average Dividend Yield (%)",
                    "Performance 5Y (%)",
                    "Market Capitalization",
                    "Debt-to-Equity Ratio",
                    "Beta",
                    "Volatility 5Y (%)",
                    "Index"
                ]

                stocks = top10_cosine_similarity.loc[:, columns_to_show].values.tolist() 

                return stocks
