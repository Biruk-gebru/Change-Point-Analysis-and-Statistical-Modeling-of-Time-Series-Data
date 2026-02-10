
from flask import Blueprint, jsonify
from .services import DataService

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/prices', methods=['GET'])
def get_prices():
    """Endpoint: /api/prices"""
    try:
        data = DataService.get_prices()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/events', methods=['GET'])
def get_events():
    """Endpoint: /api/events"""
    try:
        data = DataService.get_events()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/changepoint', methods=['GET'])
def get_changepoint_summary():
    """Endpoint: /api/changepoint"""
    try:
        summary = DataService.get_changepoint_summary()
        return jsonify(summary)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/changepoint/trace', methods=['GET'])
def get_changepoint_trace():
    """Endpoint: /api/changepoint/trace"""
    try:
        data = DataService.get_changepoint_trace()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/volatility', methods=['GET'])
def get_volatility():
    """Endpoint: /api/volatility"""
    try:
        data = DataService.get_volatility_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
