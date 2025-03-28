from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Ensure the parent directory is in Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import monte_carlo_sim
except ImportError as e:
    logger.error(f"Could not import monte_carlo_sim: {e}")
    monte_carlo_sim = None

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_simulations', methods=['GET'])
def get_available_simulations():
    simulations = [
        'quran_scientific_accuracy',
        'prophet_truthfulness',
        'tawheed_probability',
        'quran_preservation',
        'dawah_timing'
    ]
    return jsonify(simulations)

@app.route('/simulate', methods=['POST'])
def run_simulation():
    if monte_carlo_sim is None:
        return jsonify({
            'success': False,
            'error': 'Monte Carlo simulation module not imported'
        }), 500
    
    data = request.get_json()
    simulation_type = data.get('type', 'default')
    iterations = data.get('iterations', 10000)
    
    try:
        results = monte_carlo_sim.run_simulation(simulation_type, iterations)
        return jsonify({
            'success': True,
            'results': results
        })
    except Exception as e:
        logger.error(f"Simulation error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Add this route to handle GET requests (for debugging)
@app.route('/simulate', methods=['GET'])
def simulate_get():
    return jsonify({
        'error': 'Use POST method to run simulation',
        'allowed_methods': ['POST']
    }), 405

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=5000, debug=True)