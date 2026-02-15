
import pandas as pd
import os
import logging
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

class DataService:
    @staticmethod
    def get_prices(start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Reads historical Brent Oil Prices.
        
        Args:
            start_date: Optional filter start date (YYYY-MM-DD)
            end_date: Optional filter end date (YYYY-MM-DD)
            
        Returns:
            List of dictionaries containing Date and Price.
        """
        file_path = os.path.join(DATA_DIR, 'raw', 'BrentOilPrices.csv')
        if not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            return []
            
        try:
            df = pd.read_csv(file_path)
            df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
            
            # Sort and filter
            df = df.sort_values('Date')
            if start_date:
                df = df[df['Date'] >= start_date]
            if end_date:
                df = df[df['Date'] <= end_date]
                
            logger.info(f"Loaded {len(df)} price records.")
            # Convert to list of dicts for JSON
            return df[['Date', 'Price']].astype({'Date': 'str'}).to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error loading prices: {e}")
            return []

    @staticmethod
    def get_events() -> List[Dict[str, Any]]:
        """
        Reads Geopolitical Events.
        
        Returns:
            List of dictionaries containing Event data.
        """
        file_path = os.path.join(DATA_DIR, 'events', 'geopolitical_events.csv')
        if not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            return []
            
        try:
            df = pd.read_csv(file_path)
            # Ensure consistent date format
            df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
            logger.info(f"Loaded {len(df)} events.")
            return df.astype({'Date': 'str'}).to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error loading events: {e}")
            return []

    @staticmethod
    def get_changepoint_summary() -> Dict[str, float]:
        """
        Reads change point summary statistics.
        
        Returns:
            Dict mapping metrics to values.
        """
        file_path = os.path.join(RESULTS_DIR, 'statistics', 'stat_change_point_impact.csv')
        if not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            return {}
            
        try:
            df = pd.read_csv(file_path)
            # Convert to a simple key-value dict
            return dict(zip(df['Metric'], df['Value']))
        except Exception as e:
            logger.error(f"Error loading changepoint summary: {e}")
            return {}

    @staticmethod
    def get_changepoint_trace() -> List[Dict[str, Any]]:
        """
        Reads the raw changepoint trace summary (from PyMC).
        
        Returns:
            List of trace parameters.
        """
        file_path = os.path.join(DATA_DIR, 'processed', 'change_point_summary.csv')
        if not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            return []
        
        try:
            df = pd.read_csv(file_path, index_col=0)
            # Reset index to make 'parameter' a column
            df = df.reset_index().rename(columns={'index': 'parameter'})
            return df.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error loading changepoint trace: {e}")
            return []

    @staticmethod
    def get_volatility_data() -> List[Dict[str, Any]]:
        """
        Reads the stochastic volatility estimates.
        
        Returns:
            List of volatility estimates.
        """
        file_path = os.path.join(DATA_DIR, 'processed', 'stochastic_volatility_estimates.csv')
        if not os.path.exists(file_path):
            logger.warning(f"File not found: {file_path}")
            return []
            
        try:
            df = pd.read_csv(file_path)
            # Assuming format: Date, Volatility or similar
            return df.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error loading volatility data: {e}")
            return []
