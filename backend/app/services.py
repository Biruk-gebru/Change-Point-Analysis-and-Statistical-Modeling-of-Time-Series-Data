
import pandas as pd
import os
import json

# Define base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

class DataService:
    @staticmethod
    def get_prices(start_date=None, end_date=None):
        """Reads historical Brent Oil Prices."""
        file_path = os.path.join(DATA_DIR, 'raw', 'BrentOilPrices.csv')
        if not os.path.exists(file_path):
            return []
            
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
        
        # Sort and filter
        df = df.sort_values('Date')
        if start_date:
            df = df[df['Date'] >= start_date]
        if end_date:
            df = df[df['Date'] <= end_date]
            
        # Convert to list of dicts for JSON
        return df[['Date', 'Price']].astype({'Date': 'str'}).to_dict(orient='records')

    @staticmethod
    def get_events():
        """Reads Geopolitical Events."""
        file_path = os.path.join(DATA_DIR, 'events', 'geopolitical_events.csv')
        if not os.path.exists(file_path):
            return []
            
        df = pd.read_csv(file_path)
        # Ensure consistent date format
        df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
        return df.astype({'Date': 'str'}).to_dict(orient='records')

    @staticmethod
    def get_changepoint_summary():
        """Reads change point summary statistics."""
        file_path = os.path.join(RESULTS_DIR, 'statistics', 'stat_change_point_impact.csv')
        if not os.path.exists(file_path):
            return {}
            
        df = pd.read_csv(file_path)
        # Convert to a simple key-value dict
        return dict(zip(df['Metric'], df['Value']))

    @staticmethod
    def get_changepoint_trace():
        """Reads the raw changepoint trace summary (from PyMC)."""
        file_path = os.path.join(DATA_DIR, 'processed', 'change_point_summary.csv')
        if not os.path.exists(file_path):
            return []
        
        df = pd.read_csv(file_path, index_col=0)
        # Reset index to make 'parameter' a column
        df = df.reset_index().rename(columns={'index': 'parameter'})
        return df.to_dict(orient='records')

    @staticmethod
    def get_volatility_data():
        """Reads the stochastic volatility estimates."""
        file_path = os.path.join(DATA_DIR, 'processed', 'stochastic_volatility_estimates.csv')
        if not os.path.exists(file_path):
            return []
            
        df = pd.read_csv(file_path)
        # Assuming format: Date, Volatility or similar
        return df.to_dict(orient='records')
