# service_a.py

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_service', methods=['POST'])
def test_service():
    option = request.form.get('option', 'success')
    delay = request.form.get('delay') == 'true'
    delay_interval = int(request.form.get('delay_interval', '0'))
    timeout = int(request.form.get('timeout', '10'))

    params = {
        'option': option,
        'delay': 'true' if delay else 'false',
        'delay_interval': delay_interval
    }

    headers = {
        'X-Request-Retry': 'true'
    }

    try:
        response = requests.get('http://service-b:5001/test', params=params, headers=headers, timeout=timeout)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "failure", "reason": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
