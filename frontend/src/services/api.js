
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

export const fetchPrices = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/prices`);
        return response.data;
    } catch (error) {
        console.error("Error fetching prices:", error);
        return [];
    }
};

export const fetchEvents = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/events`);
        return response.data;
    } catch (error) {
        console.error("Error fetching events:", error);
        return [];
    }
};

export const fetchChangePoint = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/changepoint`);
        return response.data;
    } catch (error) {
        console.error("Error fetching changepoint:", error);
        return null;
    }
};

export const fetchVolatility = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/volatility`);
        return response.data;
    } catch (error) {
        console.error("Error fetching volatility:", error);
        return [];
    }
};
