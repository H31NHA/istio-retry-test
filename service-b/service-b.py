# service_b.py

from flask import Flask, request, jsonify
import time
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/test', methods=['GET'])
def test():
    option = request.args.get('option', 'success').lower()
    delay = request.args.get('delay', 'false').lower() == 'true'
    delay_interval = int(request.args.get('delay_interval', '0'))

    # Randomly choose between success and failure if 'random' option is selected
    if option == 'random':
        option = random.choice(['success', 'failure'])

    try:
        if delay:
            logging.info(f"Delaying response for {delay_interval} seconds")
            time.sleep(delay_interval)

        if option == 'success':
            return jsonify({"status": "success"}), 200
        elif option == 'failure':
            return jsonify({"status": "failure"}), 500
        else:
            return jsonify({"status": "invalid option"}), 400
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"status": "error", "reason": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
