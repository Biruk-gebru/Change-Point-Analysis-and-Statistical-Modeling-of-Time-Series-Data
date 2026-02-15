
def test_prices_endpoint(client):
    """Test that the prices endpoint returns 200 and a list."""
    response = client.get('/api/prices')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_events_endpoint(client):
    """Test that the events endpoint returns 200 and a list."""
    response = client.get('/api/events')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_changepoint_endpoint(client):
    """Test that the changepoint endpoint returns 200 and a dictionary."""
    response = client.get('/api/changepoint')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
