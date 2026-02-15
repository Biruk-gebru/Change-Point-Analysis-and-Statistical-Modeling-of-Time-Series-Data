
from flask import Blueprint, jsonify, Response
from typing import Tuple, Union
import logging
from .services import DataService

# Configure logging
logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/prices', methods=['GET'])
def get_prices() -> Tuple[Response, int]:
    """
    Endpoint: /api/prices
    Returns historical price data.
    """
    try:
        data = DataService.get_prices()
        logger.info(f"Serving {len(data)} price records.")
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error serving prices: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/events', methods=['GET'])
def get_events() -> Tuple[Response, int]:
    """
    Endpoint: /api/events
    Returns geopolitical events.
    """
    try:
        data = DataService.get_events()
        logger.info(f"Serving {len(data)} events.")
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error serving events: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/changepoint', methods=['GET'])
def get_changepoint_summary() -> Tuple[Response, int]:
    """
    Endpoint: /api/changepoint
    Returns change point analysis summary.
    """
    try:
        summary = DataService.get_changepoint_summary()
        logger.info("Serving changepoint summary.")
        return jsonify(summary), 200
    except Exception as e:
        logger.error(f"Error serving changepoint summary: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/changepoint/trace', methods=['GET'])
def get_changepoint_trace() -> Tuple[Response, int]:
    """
    Endpoint: /api/changepoint/trace
    Returns MCMC trace data.
    """
    try:
        data = DataService.get_changepoint_trace()
        logger.info(f"Serving {len(data)} trace records.")
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error serving changepoint trace: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/volatility', methods=['GET'])
def get_volatility() -> Tuple[Response, int]:
    """
    Endpoint: /api/volatility
    Returns volatility estimates.
    """
    try:
        data = DataService.get_volatility_data()
        logger.info(f"Serving {len(data)} volatility records.")
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error serving volatility: {e}")
        return jsonify({'error': str(e)}), 500
