# app.py
from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Define the data directory
DATA_DIR = os.path.join(app.root_path, 'data')

@app.route('/')
def index():
    """Renders the main dashboard page."""
    return render_template('index.html')

@app.route('/api/marketShare')
def get_market_share():
    """Reads and returns market share data from JSON."""
    try:
        with open(os.path.join(DATA_DIR, 'marketShare.json'), 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Market share data not found"}), 404

@app.route('/api/revenueTrends')
def get_revenue_trends():
    """Reads and returns revenue trends data from JSON."""
    try:
        with open(os.path.join(DATA_DIR, 'revenueTrends.json'), 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Revenue trends data not found"}), 404

@app.route('/api/marketSegmentation')
def get_market_segmentation():
    """Reads and returns market segmentation data from JSON."""
    try:
        with open(os.path.join(DATA_DIR, 'marketSegmentation.json'), 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Market segmentation data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
