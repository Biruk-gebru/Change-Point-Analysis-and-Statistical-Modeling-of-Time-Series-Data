
import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from app.services import DataService

@pytest.fixture
def mock_read_csv():
    with patch('pandas.read_csv') as mock:
        yield mock

def test_get_prices_file_not_found():
    """Test get_prices returns empty list if file does not exist."""
    with patch('os.path.exists', return_value=False):
        result = DataService.get_prices()
        assert result == []

def test_get_prices_success(mock_read_csv):
    """Test get_prices returns correct data structure."""
    with patch('os.path.exists', return_value=True):
        # Mock DataFrame
        mock_df = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-02'],
            'Price': [80.5, 81.2]
        })
        mock_read_csv.return_value = mock_df
        
        result = DataService.get_prices()
        
        assert len(result) == 2
        assert result[0]['Date'] == '2023-01-01'
        assert result[0]['Price'] == 80.5

def test_get_prices_filter_date(mock_read_csv):
    """Test get_prices filters by date."""
    with patch('os.path.exists', return_value=True):
        mock_df = pd.DataFrame({
            'Date': pd.to_datetime(['2023-01-01', '2023-01-05']),
            'Price': [80.5, 82.0]
        })
        mock_read_csv.return_value = mock_df
        
        # Note: In the real service, read_csv happens first, then filtering.
        # But we are mocking read_csv return value. 
        # The service converts 'Date' column to datetime. 
        # We need to ensure our mock behaves like the real DF after read_csv.
        
        # However, the service calls pd.to_datetime on the result of read_csv.
        # So we should return a DF with strings if we want to test exactly.
        
        mock_df_raw = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-05'],
            'Price': [80.5, 82.0]
        })
        mock_read_csv.return_value = mock_df_raw
        
        result = DataService.get_prices(start_date='2023-01-04')
        assert len(result) == 1
        assert result[0]['Price'] == 82.0

def test_get_events_success(mock_read_csv):
    """Test get_events returns correct data."""
    with patch('os.path.exists', return_value=True):
        mock_df = pd.DataFrame({
            'Date': ['2023-01-01'],
            'Event': ['Test Event'],
            'Category': ['Test']
        })
        mock_read_csv.return_value = mock_df
        
        result = DataService.get_events()
        assert len(result) == 1
        assert result[0]['Event'] == 'Test Event'

